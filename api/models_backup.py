from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Client(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cFlag = models.IntegerField()
    sFlag = models.IntegerField()
    website = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = (('userid', 'username'))

    #def __str__(self):
    #    return self.userid + " " + self.username + " " + self.password + " " + self.phonenumber + " " + self.name + " " + self.cFlag + " " + self.sFlag + " " + self.website

class Collectible(models.Model):
    collectible_object_id = models.IntegerField()
    collectible_content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    collectibleID = GenericForeignKey('collectible_content_type', 'collectible_object_id')
    name = models.CharField(max_length=50, default="")
    type = models.CharField(max_length=20, default="")
    year = models.IntegerField(default=1900)

    def __str__(self):
        return self.name + " " + self.type + " " + self.year


class Album(Collectible):
    artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " by " + self.artist + " - " + self.type + " " + self.year


class AlbumGenre(models.Model):
    albumID = models.ForeignKey(
        Album, related_name='genre', on_delete=models.CASCADE, default=-1)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class ComicBook(Collectible):
    author = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " written by " + self.author + " illustrated by " + self.illustrator + " - " + self.type + " " + self.year


class ComicGenre(models.Model):
    comicID = models.ForeignKey(
        ComicBook, related_name='genre', on_delete=models.CASCADE, default=-1)
    genre = models.CharField(max_length=20)

    #def __str__(self):
    #    return self.comicID + " " + self.genre


class SportCard(Collectible):
    sport = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.sport + " " + self.type + " " + self.year


class Custom(Collectible):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + " " + self.type + " " + self.year + " " + self.description

class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    sourceAddress = models.CharField(max_length=50)
    totalValue = models.IntegerField()
    userID = models.IntegerField()
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.orderId + " " + self.sourceAddress + " " + self.totalValue + " " + self.userID + " " + self.userName


class Fulfills(models.Model):

    userID = models.ForeignKey(
        Client, related_name='userIDFullfills', on_delete=models.CASCADE, default=-1)
    userName = models.ForeignKey(
        Client, related_name='usernameFullfills', on_delete=models.CASCADE, default=-1)
    orderID = models.ForeignKey(
        Order, related_name='orderIDFullfills', on_delete=models.CASCADE, default=-1)
    shippingCost = models.FloatField()

    class Meta:
        unique_together = (('userID', 'userName', 'orderID'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.orderID+" " + self.shippingCost


class Payment(models.Model):
    paymentNo = models.IntegerField(primary_key=True)
    totalValue = models.FloatField()
    formOfPayment = models.CharField(max_length=50)
    orderID = models.ForeignKey(
        Order, related_name='orderIDPayment', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.paymentNo + " " + self.totalValue + " " + self.formOfPayment + " " + self.orderID

class Admin(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.userName + " " + self.password

class Deals_With(models.Model):

    orderID = models.ForeignKey(
        Order, related_name='orderIDDealsWith', on_delete=models.CASCADE, default=-1)
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameDealsWith', on_delete=models.CASCADE, default=-1)
    
    class Meta:
        unique_together = (('orderID', 'adminUsername'))

    def __str__(self):
        return self.adminUsername + " " + self.orderID

class Manages(models.Model):

    model = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    id = GenericForeignKey('model', 'id')
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameManages', on_delete=models.CASCADE, default=-1)   

    class Meta:
        unique_together = (('model', 'adminUsername'))

    def __str__(self):
        return self.id + " " + self.adminUsername


class Collection(models.Model):
    collection_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.collection_name

class Forms(models.Model):
    collectible_id = GenericRelation(Collectible)
    collection_name = models.ForeignKey(
        Collection, related_name='collectionNameForms', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.id + " " + self.collection_name


class Made_Of(models.Model):
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    id = GenericForeignKey('model', 'id')
    order_id = models.ForeignKey(
        Order, related_name='orderIdMadeOf', on_delete=models.CASCADE, default=-1)
   
    class Meta:
        unique_together = (('model', 'order_id'))


    def __str__(self):
        return self.id + " " + self.order_id

class Wants(models.Model):

    userID = models.ForeignKey(
        Client, related_name='userIDwants', on_delete=models.CASCADE, default=-1) 
    userName = models.ForeignKey(
        Client, related_name='usernameWants', on_delete=models.CASCADE, default=-1)     
    collectionName = models.ForeignKey(
        Collection, related_name='collectionNameWants', on_delete=models.CASCADE, default=-1) 

    class Meta:
        unique_together = (('userID', 'userName', 'collectionName'))

    def __str__(self):
        return self.userID + " " + self.username + " " + self.collectionName


class Sells(models.Model):

    userID = models.ForeignKey(
        Client, related_name='userIDSells', on_delete=models.CASCADE, default=-1) 
    username = models.ForeignKey(
        Client, related_name='usernameSells', on_delete=models.CASCADE, default=-1) 
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    id = GenericForeignKey('model', 'id')
    price = models.FloatField()

    class Meta:
        unique_together = (('userID', 'model', 'username'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.id + " " + self.price

class UserCollection(models.Model):

    userName = models.ForeignKey(
        Client, related_name='usernameUserCollection', on_delete=models.CASCADE, default=-1) 
    userID = models.ForeignKey(
        Client, related_name='userIDUserCollection', on_delete=models.CASCADE, default=-1) 
    collectionName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'userName','collectionName'))

    def __str__(self):
        return self.userID + " " + self.username + " " + self.collectionName

class Consists_Of(models.Model):

    userID = models.ForeignKey(
        UserCollection, related_name='userIDConsists_Of', on_delete=models.CASCADE, default=-1) 
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    id = GenericForeignKey('model', 'id')
    collectionName = models.ForeignKey(
        UserCollection, related_name='collectionNameConsists_Of', on_delete=models.CASCADE, default=-1) 

    class Meta:
        unique_together = (('userID', 'model','collectionName'))

    def __str__(self):
        return self.userID + " " + self.id + " " + self.collectionName



class Moderates(models.Model):
    
    userID = models.ForeignKey(
        Client, related_name='userIDModerates', on_delete=models.CASCADE, default=-1) 
    username = models.ForeignKey(
        Client, related_name='usernameModerates', on_delete=models.CASCADE, default=-1) 
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameModerates', on_delete=models.CASCADE, default=-1) 

    class Meta:
        unique_together = (('userID', 'username','adminUsername'))

    def __str__(self):
        return self.userID + " " + self.username + " " + self.adminUsername


class Warehouse (models.Model):
    address = models.CharField(max_length=50)
    warehouseNumber = models.IntegerField(default=-1, unique=True)
    username = models.ForeignKey(
        Client, related_name='usernameWarehouse', on_delete=models.CASCADE, unique=False, default=-1)
    userID = models.ForeignKey(
        Client, related_name='userIDWarehouse', unique=False, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return self.address + " " + self.warehouseNumber + " " + self.username + " " + self.userID


class Shipping_Method(models.Model):

    username = models.ForeignKey(
        Client, related_name='usernameShipping_Method', on_delete=models.CASCADE, default=-1)
    userID = models.ForeignKey(
        Client, related_name='userIDShipping_Method', on_delete=models.CASCADE, default=-1)
    shippingMethod = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'username'))

    def __str__(self):
        return self.userID + " " + self.username + " " + self.shippingMethod