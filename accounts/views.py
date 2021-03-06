from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer, UserIndexSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.serializers import JSONWebTokenSerializer

# Create your views here.
@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserIndexSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    error = UserSerializer.validate(get_user_model(), data=request.data)
    if error['password'] or error['username']:
        return Response(error, status=400)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = UserSerializer.create(get_user_model(), request.data)
        serializer = UserSerializer(user)
        return Response(serializer.data)