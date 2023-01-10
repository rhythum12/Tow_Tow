from django.shortcuts import render
from rest_framework.response import Response
from .models import Billbook
from rest_framework.decorators import api_view
from user.models import User

from .BillBookSerializer import BillBookSerializer
# Create your views here.
@api_view(['GET'])
def index(req):
    bilbook=Billbook.objects.all()
    serializer= BillBookSerializer(billbook,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserBillBook(req,user_id,category):
    billbook=Billbook.objects.filter(user__id=user_id,status=category)
    print(billbook)
    serializer= BillBookSerializer(billbook,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBillbook(req,id):
    billbook=Billbook.objects.get(id=id)
    serializer=BillBookSerializer(billbook,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postBillBook(req):
    print(req.data)
    user=User.objects.get(id=req.data["user"]["id"])
    serializer=BillBookSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save(user=user)
    return Response(serializer.data)



@api_view(['POST'])
def updateBillBook(req,id):
    billbook = billbook.objects.get(id=id)
    serializer=BillBookSerializer(instance=billbook,data=req.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBillBook(req,id):
    billbook=Billbook.objects.get(id=id)
    billbook.delete()
    return Response('Deleted')


