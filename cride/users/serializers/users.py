"""Users serializers."""


# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from cride.users.models import User

# lo utiliza para obtener
class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        # para que sea compartido con los serializer    
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        # get or create = kiere decir que la tabla es de uno a uno tonces 
        # si existe obtiene y si no lo crea
        # self.context['user'] > kiere decir que obtiene de context 
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

# lo utiliza para devolver 
class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )

        




