from django.shortcuts import render
from rest_framework.response import Response
from .models import Servicing
from rest_framework.decorators import api_view
from user.models import User

from .ServicingSerializer import ServicingSerializer
# Create your views here.
@api_view(['GET'])
def index(req):
    servicing=Servicing.objects.all()
    serializer= ServicingSerializer(servicing,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserServicing(req,user_id,category):
    servicing=Servicing.objects.filter(user__id=user_id,status=category)
    print(servicing)
    serializer= ServicingSerializer(servicing,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getServicing(req,id):
    servicing=Servicing.objects.get(id=id)
    serializer=ServicingSerializer(servicing,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postServicing(req):
    print(req.data)
    user=User.objects.get(id=req.data["user"]["id"])
    serializer=ServicingSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)



@api_view(['POST'])
def updateServicing(req,id):
    servicing = Servicing.objects.get(id=id)
    serializer=Servicing(instance=servicing,data=req.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteServicing(req,id):
    servicing=Servicing.objects.get(id=id)
    servicing.delete()
    return Response('Deleted')


