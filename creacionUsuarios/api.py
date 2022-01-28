from rest_framework.response import Response
from creacionUsuarios.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)