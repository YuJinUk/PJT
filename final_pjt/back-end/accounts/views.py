from django.contrib.auth.models import User
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Accounts
from .serializers import UserListSerializer, UserSerializer, UserNicknameSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from collections import OrderedDict

@api_view(['GET'])
def user_list(request):
    users = Accounts.objects.all()
    serialized_users = UserListSerializer(users, many=True)
    print(serialized_users.data)
    return Response(serialized_users.data)

@api_view(['GET', 'PATCH'])
# @renderer_classes([JSONRenderer])
def user_profile(request, username):
    user = get_object_or_404(Accounts, username=username)
    if request.method == 'GET':
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)
    elif request.method == 'PATCH':
        serialized_user = UserSerializer(user, data=request.data)
        if serialized_user.is_valid(raise_exception=True):
            serialized_user.save()
            return Response(serialized_user.data)
        
@api_view(['GET'])
def user_nickname(request):
    users = get_list_or_404(Accounts)
    serialized_users = UserNicknameSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(['POST'])
def login(request):
    # print(request.data)
    pass

# @api_view(['POST'])
# def logout(request):
#     pass