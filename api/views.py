from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.
class ClientList (APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer (clients, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):

    def get(self, request, pk, format=None):
        client = Client.objects.get (pk=pk)
        serializer = ClientSerializer(client)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        client = Client.objects.filter(pk=pk).first()
        serializer = ClientSerializer(client, data=request.data)
        print(client)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = Client.objects.filter (pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlbumList(APIView):

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumGenreSerializer(albums, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlbumGenreSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)