from django.db import models

# Create your models here.


class Client(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cFlag = models.IntegerField
    sFlag = models.IntegerField
    website = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userid', 'username'))

    def __str__(self):
        return self.username


class Collectible(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField

    class Meta:
        abstract = True

    def __str__(self):
        return self.name + " " + self.type + " " + self.year


class Album(Collectible):
    artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " by " + self.artist + " - " + self.type + " " + self.year


class AlbumGenre(models.Model):
    albumID = models.ForeignKey(
        Album, related_name='genre', on_delete=models.CASCADE, default=1)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class ComicBook(Collectible):
    author = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " written by " + self.author + "illustrated by " + self.illustrator + " - " + self.type + " " + self.year


class ComicGenre(models.Model):
    comicID = models.ForeignKey(
        ComicBook, related_name='genre', on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class SportCard(Collectible):
    sport = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.sport + " " + self.type + " " + self.year


class Custom(Collectible):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + " " + self.type + " " + self.year + " " + self.description


class Forms(models.Model):
    id = models.IntegerField(primary_key=True)
    collection_name = models.CharField(max_length=50)

    def __str__(self):
        return self.id + " " + self.collection_name


class Made_Of(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=50)

    def __str__(self):
        return self.id + " " + self.order_id


class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    sourceAddress = models.CharField(max_length=50)
    totalValue = models.IntegerField
    userID = models.IntegerField
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.orderId + " " + self.sourceAddress + " " + self.totalValue + " " + self.userID + " " + self.userName


class Fulfills(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    orderID = models.IntegerField(unique=True)
    shippingCost = models.IntegerField

    class Meta:
        unique_together = (('userID', 'userName', 'orderID'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.orderID+" " + self.shippingCost


class Payment(models.Model):
    paymentNo = models.IntegerField(primary_key=True)
    totalValue = models.IntegerField
    formOfPayment = models.CharField(max_length=50)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.paymentNo + " " + self.totalValue + " " + self.formOfPayment + " " + self.orderID


class Deals_With(models.Model):
    adminUserName = models.CharField(max_length=50)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.adminUserName + " " + self.orderID


class Admin(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.userName + " " + self.password


class Manages(models.Model):
    ID = models.IntegerField(primary_key=True)
    adminUserName = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = (('ID', 'adminUserName'))

    def __str__(self):
        return self.ID + " " + self.adminUserName


class Collection(models.Model):
    collection_name = models.CharField(max_length=50)

    def __str__(self):
        return self.collection_name


class Wants(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    collectionName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'userName'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.collectionName


class Sells(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    ID = models.IntegerField(unique=True)
    price = models.FloatField
    collectionName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'ID', 'userName'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.ID + " " + self.price + " " + self.collectionName


class Consists_Of(models.Model):
    userID = models.IntegerField(primary_key=True)
    ID = models.IntegerField(unique=True)

    class Meta:
        unique_together = (('userID', 'ID'))

    collectionName = models.CharField(max_length=50)

    def __str__(self):
        return self.userID + " " + self.ID + " " + self.collectionName


class UserCollection(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    collectionName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'userName'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.collectionName


class Moderates(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    adminUserName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'userName'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.adminUserName


class Warehouse (models.Model):
    address = models.CharField(max_length=50)
    warehouseNumber = models.IntegerField
    userName = models.CharField(max_length=50, unique=True)
    userID = models.IntegerField(primary_key=True)

    class Meta:
        unique_together = (('userID', 'userName'))

    def __str__(self):
        return self.address + " " + self.warehouseNumber + " " + self.userName + " " + self.userID


class Shipping_Method(models.Model):
    userID = models.CharField(max_length=50, primary_key=True)
    userName = models.CharField(max_length=50, unique=True)
    shippingMethod = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userID', 'userName'))

    def __str__(self):
        return self.userID + " " + self.userName + " " + self.shippingMethod