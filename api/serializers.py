from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        exclude = ['id']

class AlbumGenreSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = models.Album
        exclude = ['id']