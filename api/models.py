from django.db import models

# Create your models here.
class Client(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cFlag = models.IntegerField
    sFlag = models.IntegerField
    website = models.CharField(max_length=50)

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
    albumID = models.ForeignKey(Album, related_name='genre', on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre

class ComicBook(Collectible):
    author = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " written by " + self.author + "illustrated by " + self.illustrator + " - " + self.type + " " + self.year

class ComicGenre(models.Model):
    comicID = models.ForeignKey(ComicBook, on_delete=models.CASCADE)
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

