from logging import exception
import os
from re import T
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from primerApp.settings import REST_FRAMEWORK
from rest_framework import status
from rest_framework import exceptions
# Importaciones de modelos agregados
from loadImage.models import SegundaTabla
# Importaciones de serializadores
from loadImage.serializer import SegundaTablaSerializer
# Importacion de JSON
import json
# Variables declaradas



# Create your views here.
class SegundaTablaList(APIView):
    
    def response_custom(self, serializer, response, state):
        responseOne = { "messages":response, "pay_load":serializer, "status":state }
        responseTwo = json.dumps(responseOne)
        responseOk = json.loads(responseTwo)
        return responseOk

    def get(self, request, format=None):
        queryset=SegundaTabla.objects.all()
        serializer=SegundaTablaSerializer(queryset, many=True, context={'request':request})
        responseOk = self.response_custom(serializer.data, "Sucess", status.HTTP_200_OK)
        return Response(responseOk)

    def post(self, request, format=None):
        if 'url_img' not in request.data:
            raise exceptions.ParseError("No hay imagen que subir")
        imagen = request.data['url_img']
        nameImg, formatImg = os.path.splitext(imagen.name)
        request.data['name_img'] = nameImg
        request.data['format_img'] = formatImg
        serializer = SegundaTablaSerializer(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            imgInf = SegundaTabla(**validated_data)
            imgInf.save()
            serializerR = SegundaTablaSerializer(imgInf)
            return Response(self.response_custom(serializerR.data, "Sucess", status.HTTP_201_CREATED))
        return Response(self.response_custom(serializer.errors, "Error", status.HTTP_400_BAD_REQUEST))
        
    
class SegundaTablaDetail(APIView):

    def get_object(self, pk):
        try:
            return SegundaTabla.objects.get(pk = pk)
        except SegundaTabla.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = SegundaTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if 'url_img' not in request.data:
            raise exceptions.ParseError("No hay imagen que subir")
        imagen = request.data['url_img']
        nameImg, formatImg = os.path.splitext(imagen.name)
        request.data['name_img'] = nameImg
        request.data['format_img'] = formatImg
        serializer = SegundaTablaSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idObject = self.get_object(pk)
        if idObject != "No existe":
            idObject.delete()
            return Response("Eliminado", status = status.HTTP_200_OK)
        else:
            return Response("Id no encontrado", status = status.HTTP_400_BAD_REQUEST)