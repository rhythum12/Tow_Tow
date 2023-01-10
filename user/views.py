from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .UserSerializer import UserSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(req):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserById(req,uid):
    print(uid)
    user=User.objects.filter(uid=uid)
    print(user)
    if(user.count()>0):
        serializer=UserSerializer(user[0],many=False)
        return Response(serializer.data)
    else:
        return Response(status=404)

@api_view(['POST'])
def postUser(req):
    serializer=UserSerializer(data=req.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def updateUser(req,id):
    print(req.data)
    user=User.objects.get(id=id)
    serializer=UserSerializer(instance=user,data=req.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(req,uid):
    user=User.objects.get(uid=id)
    user.delete()
    return Response('Deleted')
