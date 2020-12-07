from django.db.models import fields
from rest_framework import serializers
from . import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

class AlbumGenreSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(max_length=20)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        genre_representation = representation.pop('genre')
        return genre_representation

    class Meta:
        model = models.AlbumGenre
        fields = ('genre',)

class AlbumSerializer(serializers.ModelSerializer):
    genre = AlbumGenreSerializer(many=True)

    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        album = models.Album.objects.create(**validated_data)
        for genre_data in genres_data:
            models.AlbumGenre.objects.create(albumID=album, **genre_data)
        return album

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genre')
        genres = (instance.genre).all()
        genres = list(genres)
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.year = validated_data.get('year', instance.year)
        instance.save()

        for genre_data in genres_data:
            genre = genres.pop(0)
            genre.albumID = genre_data.get('albumID', genre.albumID)
            genre.genre = genre_data.get('genre', genre.genre)
            genre.save()
        return instance

    class Meta:
        model = models.Album
        fields = ('id', 'name', 'artist', 'genre', 'year', )


class ComicGenreSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(max_length=20)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        genre_representation = representation.pop('genre')
        return genre_representation

    class Meta:
        model = models.ComicGenre
        fields = ('genre', )


class ComicBookSerializer(serializers.ModelSerializer):
    genre = ComicGenreSerializer(many=True)

    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        comic = models.ComicBook.objects.create(**validated_data)
        for genre_data in genres_data:
            models.ComicGenre.objects.create(comicID=comic, **genre_data)
        return comic

    class Meta:
        model = models.ComicBook
        fields = ('id', 'name', 'author', 'illustrator', 'genre', 'year')


class SportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SportCard
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models. Custom
        fields = '__all__'

class CollectibleSerializer(serializers.RelatedField):
    
    def to_representation(self, value):
        if isinstance(value, models.Album):
            return AlbumSerializer(value).data
        elif isinstance(value, models.SportCard):
            return SportCardSerializer(value).data
        elif isinstance(value, models.ComicBook):
            return ComicBookSerializer(value).data
        return CustomSerializer(value).data

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Forms
        fields = '__all__'


class MadeOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Made_Of
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class FulfillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fulfills
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipping_Method
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = '__all__'

class ModeratesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Moderates
        fields = '__all__'

class UserCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserCollection
        fields = '__all__'

class ConsistsOfSerializer(serializers.ModelSerializer):
    id = CollectibleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Consists_Of
        fields = '__all__'

class SellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sells
        fields = '__all__'

class WantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wants
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'

class ManagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manages
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = '__all__'

class DealsWithSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deals_With
        fields = '__all__'