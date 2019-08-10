from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):

    class Meta():
        model = models.CustomerInformation
        fields = '__all__'
        
