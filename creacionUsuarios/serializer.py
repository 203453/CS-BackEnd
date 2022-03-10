from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(
           required=True,
           validators=[UniqueValidator(queryset=User.objects.all())]
           )
 
   password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
   password2 = serializers.CharField(write_only=True, required=True)
 
   class Meta:
       model = User
       fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': True},
           'last_name': {'required': True}
       }
 
   def validate(self, attrs):
       if attrs['password'] != attrs['password2']:
           raise serializers.ValidationError({"password": "Las contraseñan no coinciden."})
 
       return attrs
 
   def create(self, validated_data):
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name']
       )
 

       user.set_password(validated_data['password'])
       user.save()
 
       return user





# from django.contrib.auth.models import User
# from rest_framework import serializers

# class UserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def create(self, validate_data):
#         instance = User()
#         instance.first_name = validate_data.get('first_name')
#         instance.last_name = validate_data.get('last_name')
#         instance.username = validate_data.get('username')
#         instance.email = validate_data.get('email')
#         instance.set_password(validate_data.get('password'))
#         instance.save()
#         return instance

#     def validate_username(self, data):
#         users = User.objects.filter(username = data)
#         if len(users) != 0:
#             raise serializers.ValidationError("Usuario ya existente")
#         else:
#             return data