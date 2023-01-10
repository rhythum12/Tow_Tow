from .models import Billbook
from rest_framework import serializers

class BillBookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id') # ADD THIS LINE
    
    class Meta:
        model=Billbook
        fields="__all__"