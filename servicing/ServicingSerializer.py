from .models import Servicing
from rest_framework import serializers

class ServicingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id') # ADD THIS LINE
    
    class Meta:
        model=Servicing
        fields="__all__"