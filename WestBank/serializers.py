from rest_framework import serializers

from WestBank.models import *


class CustomprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customprofile
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'