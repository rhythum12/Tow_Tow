from django.shortcuts import render
from rest_framework.response import Response
from .models import Vehicle
from .VehicleSerializer import VechicleSerializer
from rest_framework.decorators import api_view
from user.models import User

# Create your views here.
@api_view(['GET'])
def index(req):
    vehicle=Vehicle.objects.all()
    serializer= VechicleSerializer(vehicle,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getVehicleById(req,id):
    vehicle=Vehicle.objects.get(id=id)
    serializer=VechicleSerializer(vehicle,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postVehicle(req):
    serializer=VechicleSerializer(data=req.data)
    print(req.data)
    user=User.objects.get(id=req.data["user"]["id"])
    print(user)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)



@api_view(['POST'])
def updateVehicle(req,id):
    vehicle = Vehicle.objects.get(id=id)
    serializer=VechicleSerializer(instance=vehicle,data=req.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteVehicle(req,id):
    vehicle=Vehicle.objects.get(id=id)
    vehicle.delete()
    return Response('Deleted')

@api_view(['GET'])
def getVehicleForUser(req,id):
    vehicles=Vehicle.objects.filter(user__id=id)
    serializer=VechicleSerializer(vehicles,many=True)
    return Response(serializer.data)
