"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action

# Serializers
from cride.users.serializers import (
    UserLoginSerializer, UserModelSerializer, UserSignUpSerializer, AccountVerificationSerializer
)


class UserViewSet(viewsets.GenericViewSet):
    """User view set.
    Handle sign up, login and account verification.
    """
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    # el nombre sirve para la url /signup
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go share some rides!'}
        return Response(data, status=status.HTTP_200_OK)


# class UserLoginAPIView(APIView):
#     """User login API view """

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#         data = {
#             'user': UserModelSerializer(user).data,
#             'access_token': token
#         }
#         return Response(data, status=status.HTTP_201_CREATED)


# class UserSignUpAPIView(APIView):
#     """User sign up API view """

#     def post(self, request, *args, **kwargs):
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data = UserModelSerializer(user).data,
#         return Response(data, status=status.HTTP_201_CREATED)


# class AccountVerificationAPIView(APIView):
#     """Account verification API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = AccountVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {'message': 'Congratulation, now go share some rides!'}
#         return Response(data, status=status.HTTP_200_OK)





