from django.db import models
from django.db.models.fields.related import ForeignKey


class Client(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cFlag = models.IntegerField(blank=True)
    sFlag = models.IntegerField(blank=True)
    website = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username + " " + self.password + " " + str(self.phonenumber) + " " + self.name + " " + str(self.cFlag) + " " + str(self.sFlag) + " " + self.website


class Collectible(models.Model):
    name = models.CharField(max_length=50, default="")
    type = models.CharField(max_length=20, default="")
    year = models.IntegerField(default=1900)

    def __str__(self):
        return self.name + " " + self.type + " " + str(self.year)


class Album(Collectible):
    artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " by " + self.artist + " - " + self.type + " " + str(self.year)


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
        return self.name + " written by " + self.author + " illustrated by " + self.illustrator + " - " + self.type + " " + str(self.year)


class ComicGenre(models.Model):
    comicID = models.ForeignKey(
        ComicBook, related_name='genre', on_delete=models.CASCADE, default=-1)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.comicID) + " " + self.genre


class SportCard(Collectible):
    sport = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.sport + " " + self.type + " " + str(self.year)


class Custom(Collectible):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + " " + self.type + " " + str(self.year) + " " + self.description


class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    sourceAddress = models.CharField(max_length=50)
    totalValue = models.IntegerField()
    userName = models.ForeignKey(
        Client, related_name='usernameOrder', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return str(self.orderId) + " " + self.sourceAddress + " " + str(self.totalValue) + " " + str(self.userName)


class Fulfills(models.Model):
    userName = models.ForeignKey(
        Client, related_name='usernameFullfills', on_delete=models.CASCADE, default=-1)
    orderID = models.ForeignKey(
        Order, related_name='orderIDFullfills', on_delete=models.CASCADE, default=-1)
    shippingCost = models.FloatField()

    class Meta:
        unique_together = (('userName', 'orderID'))

    def __str__(self):
        return str(self.userName) + " " + str(self.orderID) + " " + str(self.shippingCost)


class Payment(models.Model):
    paymentNo = models.IntegerField(primary_key=True)
    totalValue = models.FloatField()
    formOfPayment = models.CharField(max_length=50)
    orderID = models.ForeignKey(
        Order, related_name='orderIDPayment', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return str(self.paymentNo) + " " + str(self.totalValue) + " " + self.formOfPayment + " " + str(self.orderID)


class Admin(models.Model):
    userName = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.userName + " " + self.password


class Deals_With(models.Model):

    orderID = models.ForeignKey(
        Order, related_name='orderIDDealsWith', on_delete=models.CASCADE, default=-1)
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameDealsWith', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('orderID', 'adminUsername'))

    def __str__(self):
        return str(self.adminUsername) + " " + str(self.orderID)


class Manages(models.Model):

    collectible_id = models.ForeignKey(
        Collectible, related_name='collectionIDManage', on_delete=models.CASCADE, default=-1)
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameManages', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('collectible_id', 'adminUsername'))

    def __str__(self):
        return str(self.collectible_id) + " " + str(self.adminUsername)


class Collection(models.Model):
    collection_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.collection_name


class Forms(models.Model):
    collectible_id = models.ForeignKey(
        Collectible, related_name='collectionIDForms', on_delete=models.CASCADE, default=-1)
    collection_name = models.ForeignKey(
        Collection, related_name='collectionNameForms', on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return str(self.collectible_id) + " " + str(self.collection_name)


class Made_Of(models.Model):
    collectible_id = models.ForeignKey(
        Collectible, related_name='collectibleIDMadeOf', on_delete=models.CASCADE)
    order_id = models.ForeignKey(
        Order, related_name='orderIdMadeOf', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('collectible_id', 'order_id'))

    def __str__(self):
        return str(self.collectible_id) + " " + str(self.order_id)


class Wants(models.Model):
    userName = models.ForeignKey(
        Client, related_name='usernameWants', on_delete=models.CASCADE, default=-1)
    collectionName = models.ForeignKey(
        Collection, related_name='collectionNameWants', on_delete=models.CASCADE, default=-1)

    class Meta:
        unique_together = (('userName', 'collectionName'))

    def __str__(self):
        return str(self.userName) + " " + str(self.collectionName)


class Sells(models.Model):
    username = models.ForeignKey(
        Client, related_name='usernameSells', on_delete=models.CASCADE, default=-1)
    collectible_id = models.ForeignKey(
        Collectible, related_name='collectionIDSells', on_delete=models.CASCADE, default=-1)
    price = models.FloatField()

    class Meta:
        unique_together = (('collectible_id', 'username'))

    def __str__(self):
        return str(self.username) + " " + str(self.collectible_id) + " " + str(self.price)


class UserCollection(models.Model):

    userName = models.ForeignKey(
        Client, related_name='usernameUserCollection', on_delete=models.CASCADE, default=-1)
    collectionName = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userName', 'collectionName'))

    def __str__(self):
        return str(self.userName) + " " + self.collectionName


class Consists_Of(models.Model):

    collectible_id = models.ForeignKey(
        Collectible, related_name='collectionIDConsistsOf', on_delete=models.CASCADE)
    collectionName = models.ForeignKey(
        UserCollection, related_name='collectionNameConsists_Of', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('collectible_id', 'collectionName'))

    def __str__(self):
        return str(self.collectible_id) + " " + str(self.collectionName)


class Moderates(models.Model):
    username = models.ForeignKey(
        Client, related_name='usernameModerates', on_delete=models.CASCADE, default=-1)
    adminUsername = models.ForeignKey(
        Admin, related_name='adminUsernameModerates', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('username', 'adminUsername'))

    def __str__(self):
        return str(self.username) + " " + str(self.adminUsername)


class Warehouse (models.Model):
    address = models.CharField(max_length=50)
    warehouseNumber = models.IntegerField(default=-1, unique=True)
    username = models.ForeignKey(
        Client, related_name='usernameWarehouse', on_delete=models.CASCADE, unique=False, default=-1)

    class Meta:
        unique_together=(('warehouseNumber', 'username'))

    def __str__(self):
        return self.address + " " + str(self.warehouseNumber) + " " + str(self.username)


class Shipping_Method(models.Model):

    username = models.ForeignKey(
        Client, related_name='usernameShipping_Method', on_delete=models.CASCADE, default=-1)
    shippingMethod = models.CharField(max_length=50)

    def __str__(self):
        return str(self.username) + " " + self.shippingMethod
