from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','email','first_name','last_name','password')
#         extra_kwargs= {'password': ('write_only':True)}
    def create(selfself,validate_data):
        password = validate_data.pop('password')
        user = User(**validate_data)
        user.username = validate_data.get('email')
        user.set_password(password)
        user.save()
        return user        
