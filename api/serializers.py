from django.db.models import fields
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
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Album
        fields = '__all__'


class ComicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ComicGenre
        fields = '__all__'


class ComicBookSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.ComicBook
        fields = '__all__'


class SportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SportCard
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models. Custom
        fields = '__all__'


class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Forms
        fields = '__all__'


class MadeOFSerializer(serializers.ModelSerializer):
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