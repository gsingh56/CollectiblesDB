from rest_framework import serializers
from . import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

class AlbumGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumGenre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    genre = AlbumGenreSerializer(many=False)

    class Meta:
        model = models.Album
        fields = '__all__'