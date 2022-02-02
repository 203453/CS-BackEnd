from re import T
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from primerApp.settings import REST_FRAMEWORK
from rest_framework import status
# Importaciones de modelos agregados
from primerComponente.models import PrimerTabla
# Importaciones de serializadores
from primerComponente.serializer import PrimerTablaSerializer
# Importacion de JSON
import json

# Variables declaradas



# Create your views here.
class PrimerTablaList(APIView):

    def response_custom(self, serializer, response, state):
        responseOne = { "messages":response, "pay_load":serializer, "status":state }
        responseTwo = json.dumps(responseOne)
        responseOk = json.loads(responseTwo)
        return responseOk

    def get(self, request, format=None):
        queryset=PrimerTabla.objects.all()
        serializer=PrimerTablaSerializer(queryset, many=True, context={'request':request})
        responseOk = self.response_custom(serializer.data, "Sucess", status.HTTP_200_OK)
        return Response(responseOk)

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom(datas, "Sucess", status.HTTP_201_CREATED))
        return Response(self.response_custom(serializer.errors, "Error", status.HTTP_400_BAD_REQUEST))
        
    
class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = PrimerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = PrimerTablaSerializer(idResponse, data = request.data)
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