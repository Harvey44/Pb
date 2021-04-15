import locale
import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from WestBank.models import *
from WestBank.serializers import *


def index(request):
    return render(request, "index.html")


@login_required(login_url='login/')
def home(request):
    user = Customprofile.objects.get(username=request.user)
    serializer = CustomprofileSerializer(user, many=False)

    print(serializer.data)
    return render(request, "account/app.html", {"context": serializer.data})


@login_required(login_url='login/')
def send(request):
    user = Customprofile.objects.get(username=request.user)
    serializer = CustomprofileSerializer(user, many=False)

    print(serializer.data)
    return render(request, "account/send.html", {"context": serializer.data})


@login_required(login_url='login/')
def transfers(request):
    user = Customprofile.objects.get(username=request.user)
    transfers = Transactions.objects.filter(user=user)
    serializer = TransactionSerializer(transfers, many=True)
    print(serializer.data)
    return render(request, "account/transfers.html", {"context": serializer.data})


@login_required(login_url='login/')
def profile(request):
    user = Customprofile.objects.get(username=request.user)
    serializer = CustomprofileSerializer(user, many=False)

    return render(request, "account/profile.html", {"context": serializer.data})


@api_view(['POST'])
def post_pin(request):
    if request.method == 'POST':
        username = request.data['username']
        try:
            pin = request.data['pin']
            user = Customprofile.objects.get(username=username)
            response = ''
            if user.pin == pin:
                response = {"message": 'Success',
                            "status": True,
                            "status_code": status.HTTP_200_OK,
                            }
            else:
                response = {"message": 'Incorrect Pin',
                            "status": False,
                            "status_code": status.HTTP_401_UNAUTHORIZED,
                            }
        except Customprofile.DoesNotExist:
            response = {"message": 'Invalid Token',
                        "status": True,
                        "status_code": status.HTTP_401_UNAUTHORIZED, }
        return Response(response)
    return Response("GET NOT ALLOWED")


@api_view(['POST'])
def post_code(request):
    if request.method == 'POST':
        username = request.data['username']
        try:
            code = request.data['code']
            user = Customprofile.objects.get(username=username)
            response = ''
            if user.transfer_code == code:
                response = {"message": 'Success',
                            "status": True,
                            "status_code": status.HTTP_200_OK,
                            }
            else:
                response = {"message": 'Incorrect Transfer Code',
                            "status": False,
                            "status_code": status.HTTP_401_UNAUTHORIZED,
                            }
        except Customprofile.DoesNotExist:
            response = {"message": 'Invalid Token',
                        "status": True,
                        "status_code": status.HTTP_401_UNAUTHORIZED, }
        return Response(response)
    return Response("GET NOT ALLOWED")


@api_view(['POST'])
def post_transfer(request):
    if request.method == 'POST':
        username = request.data['username']
        try:
            user = Customprofile.objects.get(username=username)
            amount = request.data['amount']
            fullname = request.data['fullname']
            bankname = request.data['bankname']
            number = request.data['number']
            country = request.data['country']
            ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            transaction = Transactions.objects.create(user=user, fullname=fullname, amount=amount, bankname=bankname,
                                                      number=number, country=country, reference="REF " + ref,
                                                      status=True)
            user.figure -= amount
            df = locale.currency(user.figure, grouping=True)
            user.balance = df.replace("$", "").replace(".00", "")
            user.save()
            response = {"message": 'Success',
                        "status": True,
                        "status_code": status.HTTP_200_OK,
                        }
        except Customprofile.DoesNotExist:
            response = {"message": 'Invalid Token',
                        "status": True,
                        "status_code": status.HTTP_401_UNAUTHORIZED, }
        return Response(response)
    return Response("GET NOT ALLOWED")
