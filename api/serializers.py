from rest_framework import serializers
from procedures.models import Procedure
from specialists.models import Specialist
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class SpecialistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

class SpecialistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Specialist
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    is_booked = serializers.BooleanField(source='booked_by', read_only=True)
    booked_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Procedure
        fields = ['id', 'name', 'description', 'time', 'duration', 'is_booked', 'booked_by']
