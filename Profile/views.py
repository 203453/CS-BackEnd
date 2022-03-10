# Create your views here.
import json
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
import datetime
#Models
from Profile.models import TercerTabla
from django.contrib.auth.models import User


#Serializers
from Profile.serializers import TercerTablaSerializer

class TercerTablaList(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 0
    
    def post(self, request):
        if 'url_image' not in request.data:
            raise exceptions.ParseError(
                "No se ha seleccionado una imagen")
        imagen = request.data['url_image']
        id_user = request.data['id_user']
        user = self.get_objectUser(id_user)
        serializer = TercerTablaSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            profile = TercerTabla(**validated_data)
            profile.save()
            serializer_response = TercerTablaSerializer(profile)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)
    
class TercerTablaDetail(APIView):

    def get_object(self, pk):
        try:
            return TercerTabla.objects.get(id_user = pk)
        except TercerTabla.DoesNotExist:
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = TercerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_image']
        idResponse = self.get_object(pk)
        if(idResponse != 0):
            serializer = TercerTablaSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.url_image))
            except os.error:
                print("Imagen no encontrada")
            idResponse.url_image = archivos
            idResponse.save()
            return Response("Imagen actualizada", status=status.HTTP_201_CREATED)
        else:
            return Response("Error")
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile != 404:
            profile.url_image.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
    
    def res_custom(self, user, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "status" : status
        }
        return response;
    
    def get(self, request, pk, format=None):
        idResponse = User.objects.filter(id=pk).values()
        if(idResponse != 404):
            responseData = self.res_custom(idResponse, status.HTTP_200_OK)
            return Response(responseData)
        return("No se encontró el usuario")
    
    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(id = pk)
        user.update(username = data.get('username'))
        user.update(first_name = data.get('first_name'))
        user.update(last_name = data.get('last_name'))
        user.update(email = data.get('email'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.res_custom(user2, status.HTTP_200_OK))