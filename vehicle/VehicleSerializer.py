from rest_framework import serializers
from .models import Vehicle

class VechicleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id') # ADD THIS LINE
    class Meta:
        model=Vehicle
        fields="__all__"