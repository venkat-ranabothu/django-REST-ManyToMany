from django.http import JsonResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Group
from .serializers import UserSerializer, GroupSerializer


@api_view(["GET"])
@csrf_exempt
def get_groups(user_request):
    user_payload = json.loads(user_request.body)
    user = User.objects.get(user_id=user_payload["user_id"])
    groups = user.groups
    serializer = GroupSerializer(groups, many=True)
    return JsonResponse({'groups': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
def get_user_details(user_request):
    user_payload = json.loads(user_request.body)
    user = User.objects.get(user_id=user_payload["user_id"])
    serializer = UserSerializer(user)
    return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
def associate_user_to_group(request):
    payload = json.loads(request.body)
    user = User.objects.get(user_id=payload["user_id"])
    group = Group.objects.get(group_name=payload["group_name"])
    user.groups.add(group)
    serializer = GroupSerializer(group)
    return JsonResponse({'groups': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
def create_user(request):
    try:
        payload = json.loads(request.body)
        first_name = payload["first_name"]
        last_name = payload["last_name"]
        user = User(first_name=first_name, last_name=last_name)
        user.save()
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'error': 'Bad Request'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def create_group(request):
    try:
        payload = json.loads(request.body)
        group_name = payload["group_name"]
        group = Group(group_name=group_name)
        group.save()
        serializer = GroupSerializer(group)
        return JsonResponse({'group': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'error': 'Bad Request'}, status=status.HTTP_404_NOT_FOUND)
