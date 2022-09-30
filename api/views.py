from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class AdminAuthentication(APIView):
    def get(self, request, user, pwd, format=None):
        admin = Admin.objects.filter(userName=user, password=pwd)
        if(admin):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ClientAuthentication(APIView):
    def get(self, request, user, pwd, format=None):
        client = Client.objects.filter(username=user, password=pwd)
        if(client):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ClientList (APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):

    def get(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(username=user)
        elif clientname != None:
            client = Client.objects.filter(name=clientname)
        else:
            client = Client.objects.filter(phonenumber=num)
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(
                username=user).first()
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname).first()
        else:
            client = Client.objects.filter(
                phonenumber=num).first()
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(
                username=user).first()
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname).first()
        else:
            client = Client.objects.filter(
                phonenumber=num).first()
        if client == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectorList(APIView):

    def get(self, request, format=None):
        collectors = Client.objects.filter(cFlag=1)
        serializer = ClientSerializer(collectors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectorDetail(APIView):

    def get(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(username=user, cFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, cFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, cFlag=1)
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(
                username=user, cFlag=1).first()
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname, cFlag=1).first()
        else:
            client = Client.objects.filter(
                phonenumber=num, cFlag=1).first()
        serializer = ClientSerializer(client, data=request.data)
        print(client)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(
                username=user, cFlag=1)
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname, cFlag=1)
        else:
            client = Client.objects.filter(
                phonenumber=num, cFlag=1)
        if client.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerDetail(APIView):

    def get(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(username=user, sFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1)
        serializer = SellerSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(username=user, sFlag=1).first()
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1).first()
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1).first()
        serializer = SellerSerializer(client, data=request.data)
        print(client)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, clientname=None, num=None, format=None):
        if user != None:
            client = Client.objects.filter(username=user, sFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1)
        if client.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerList(APIView):

    def get(self, request, format=None):
        sellers = Client.objects.filter(sFlag=1)
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectibleList (APIView):
    def get(self, request, format=None):
        albums = Album.objects.all()
        comics = ComicBook.objects.all()
        cards = SportCard.objects.all()
        custom = Custom.objects.all()
        albumSerializer = AlbumSerializer(albums, many=True)
        comicSerializer = ComicBookSerializer(comics, many=True)
        cardSerializer = SportCardSerializer(cards, many=True)
        customSerializer = CustomSerializer(custom, many=True)
        return Response(albumSerializer.data + comicSerializer.data + 
            customSerializer.data + cardSerializer.data)

    def post(self, request, format=None):
        try:
            serializer = AlbumSerializer(data=request.data)
        except:
            try:
                serializer = ComicBookSerializer(data=request.data)
            except:
                try:
                    serializer = CustomSerializer(data=request.data)
                except:
                    serializer = SportCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectibleDetail(APIView):
    def get(self, request, id=None, collectiblename=None, collectibletype=None, release=None, format=None):
        if id != None:
            albums = Album.objects.filter(id=id)
            comics = ComicBook.objects.filter(id=id)
            cards = SportCard.objects.filter(id=id)
            custom = Custom.objects.filter(id=id)
            albumSerializer = AlbumSerializer(albums, many=True)
            comicSerializer = ComicBookSerializer(comics, many=True)
            cardSerializer = SportCardSerializer(cards, many=True)
            customSerializer = CustomSerializer(custom, many=True)
        elif collectiblename != None:
            albums = Album.objects.filter(name=collectiblename)
            comics = ComicBook.objects.filter(name=collectiblename)
            cards = SportCard.objects.filter(name=collectiblename)
            custom = Custom.objects.filter(name=collectiblename)
            albumSerializer = AlbumSerializer(albums, many=True)
            comicSerializer = ComicBookSerializer(comics, many=True)
            cardSerializer = SportCardSerializer(cards, many=True)
            customSerializer = CustomSerializer(custom, many=True)
        elif collectibletype != None:
            albums = Album.objects.filter(type=collectibletype)
            comics = ComicBook.objects.filter(type=collectibletype)
            cards = SportCard.objects.filter(type=collectibletype)
            custom = Custom.objects.filter(type=collectibletype)
            albumSerializer = AlbumSerializer(albums, many=True)
            comicSerializer = ComicBookSerializer(comics, many=True)
            cardSerializer = SportCardSerializer(cards, many=True)
            customSerializer = CustomSerializer(custom, many=True)
        else:
            albums = Album.objects.filter(year=release)
            comics = ComicBook.objects.filter(year=release)
            cards = SportCard.objects.filter(year=release)
            custom = Custom.objects.filter(year=release)
            albumSerializer = AlbumSerializer(albums, many=True)
            comicSerializer = ComicBookSerializer(comics, many=True)
            cardSerializer = SportCardSerializer(cards, many=True)
            customSerializer = CustomSerializer(custom, many=True)
        return Response(albumSerializer.data + comicSerializer.data + 
            customSerializer.data + cardSerializer.data)

    def delete(self, request, id=None, collectiblename=None, collectibletype=None, release=None, format=None):
        if id != None:
            albums = Album.objects.filter(id=id)
            comics = ComicBook.objects.filter(id=id)
            cards = SportCard.objects.filter(id=id)
            custom = Custom.objects.filter(id=id)
        elif collectiblename != None:
            albums = Album.objects.filter(name=collectiblename)
            comics = ComicBook.objects.filter(name=collectiblename)
            cards = SportCard.objects.filter(name=collectiblename)
            custom = Custom.objects.filter(name=collectiblename)
        elif collectibletype != None:
            albums = Album.objects.filter(type=collectibletype)
            comics = ComicBook.objects.filter(type=collectibletype)
            cards = SportCard.objects.filter(type=collectibletype)
            custom = Custom.objects.filter(type=collectibletype)
        else:
            albums = Album.objects.filter(year=release)
            comics = ComicBook.objects.filter(year=release)
            cards = SportCard.objects.filter(year=release)
            custom = Custom.objects.filter(year=release)
        collectible = albums or comics or cards or custom
        if collectible.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        collectible.first().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComicBookList(APIView):
    def get(self, request, format=None):
        comicBooks = ComicBook.objects.all()
        serializer = ComicBookSerializer(comicBooks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComicBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicBookDetails(APIView):
    def get(self, request, id=None, comicName=None, authorName=None, illustratorName=None,
        release=None, comicType=None, comicGenre=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id)
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName)
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName)
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
        elif comicType != None:
            comicBook = ComicBook.objects.filter(type=comicType)
        elif comicGenre != None:
            comicGenre = ComicGenre.objects.filter(genre=comicGenre)
            data = []
            for gen in comicGenre:
                comic = ComicBook.objects.filter(id=gen.comicID.id)
                data += ComicBookSerializer(comic, many=True).data
            return Response(data)
        else:
            comicBook = ComicBook.objects.filter(illustrator=illustratorName)
        serializer = ComicBookSerializer(comicBook, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, comicName=None, authorName=None, illustratorName=None,
        release=None, comicType=None, comicGenre=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id).first()
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName).first()
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName).first()
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
        elif comicGenre != None:
            comicGenre = ComicBook.objects.filter(genre=comicGenre).first()
            comicBook = comicGenre.comicID
        elif comicType != None:
            comicBook = ComicBook.objects.filter(type=comicType)
        else:
            comicBook = ComicBook.objects.filter(
                illustrator=illustratorName).first()
        serializer = ComicBookSerializer(comicBook, data=request.data)
        print(comicBook)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, comicName=None, authorName=None, illustratorName=None,
        release=None, comicType=None, comicGenre=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id)
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName)
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName)
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
        elif comicGenre != None:
            comicGenre = ComicBook.objects.filter(genre=comicGenre).first()
            comicBook = comicGenre.comicID
        elif comicType != None:
            comicBook = ComicBook.objects.filter(type=comicType)
        else:
            comicBook = ComicBook.objects.filter(illustrator=illustratorName)
        if comicBook.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comicBook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumList(APIView):

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetail(APIView):

    def get(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, albumGenre=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id)
        elif albumName != None:
            album = Album.objects.filter(name=albumName)
        elif artistName != None:
            album = Album.objects.filter(artist=artistName)
        elif albumType != None:
            album = Album.objects.filter(type=albumType)
        elif albumGenre != None:
            albumGenre = AlbumGenre.objects.filter(genre=albumGenre)
            data = []
            for gen in albumGenre:
                album = Album.objects.filter(id=gen.albumID.id)
                data += AlbumSerializer(album, many=True).data
            return Response(data)
        else:
            album = Album.objects.filter(year=release)
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, albumGenre=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id).first()
        elif albumName != None:
            album = Album.objects.filter(name=albumName).first()
        elif artistName != None:
            album = Album.objects.filter(artist=artistName).first()
        elif albumType != None:
            album = Album.objects.filter(type=albumType).first()
        elif albumGenre != None:
            albumGenre = AlbumGenre.objects.filter(genre=albumGenre).first()
            album = albumGenre.albumID
        else:
            album = Album.objects.filter(year=release).first()
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, albumGenre=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id)
        elif albumName != None:
            album = Album.objects.filter(name=albumName)
        elif artistName != None:
            album = Album.objects.filter(artist=artistName)
        elif albumType != None:
            album = Album.objects.filter(type=albumType)
        elif albumGenre != None:
            albumGenre = AlbumGenre.objects.filter(genre=albumGenre)
            album = albumGenre.albumID
        else:
            album = Album.objects.filter(year=release)
        if album.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SportCardList(APIView):
    def get(self, request, format=None):
        cards = SportCard.objects.all()
        serializer = SportCardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SportCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SportCardDetails(APIView):
    def get(self, request, id=None, cardName=None, cardType=None, sportName=None, release=None, format=None):
        if id != None:
            sport = SportCard.objects.filter(id=id)
        elif cardName != None:
            sport = SportCard.objects.filter(name=cardName)
        elif sportName != None:
            sport = SportCard.objects.filter(sport=sportName)
        elif cardType != None:
            sport = SportCard.objects.filter(type=cardType)
        else:
            sport = SportCard.objects.filter(year=release)
        serializer = SportCardSerializer(sport, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, cardName=None, cardType=None, sportName=None, release=None, format=None):
        if id != None:
            sport = SportCard.objects.filter(id=id).first()
        elif cardName != None:
            sport = SportCard.objects.filter(name=cardName).first()
        elif sportName != None:
            sport = SportCard.objects.filter(sport=sportName).first()
        elif cardType != None:
            sport = SportCard.objects.filter(type=cardType).first()
        else:
            sport = SportCard.objects.filter(year=release).first()
        serializer = SportCardSerializer(sport, data=request.data)
        print(sport)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, cardName=None, cardType=None, sportName=None, release=None, format=None):
        if id != None:
            sport = SportCard.objects.filter(id=id)
        elif cardName != None:
            sport = SportCard.objects.filter(name=cardName)
        elif sportName != None:
            sport = SportCard.objects.filter(sport=sportName)
        elif cardType != None:
            sport = SportCard.objects.filter(type=cardType)
        else:
            sport = SportCard.objects.filter(year=release)
        if sport.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomList(APIView):
    def get(self, request, format=None):
        custom = Custom.objects.all()
        serializer = CustomSerializer(custom, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomDetails(APIView):

    def get(self, request, id=None, collectibleName=None, collectibleType=None, release=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id)
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName)
        elif release != None:
            custom = Custom.objects.filter(year=release)
        else:
            custom = Custom.objects.filter(type=collectibleType)
        serializer = CustomSerializer(custom, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, collectibleName=None, collectibleType=None, release=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id).first()
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName).first()
        elif release != None:
            custom = Custom.objects.filter(year=release).first()
        else:
            custom = Custom.objects.filter(type=collectibleType).first()
        serializer = CustomSerializer(custom, data=request.data)
        print(custom)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, collectibleName=None, collectibleType=None, release=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id)
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName)
        elif release != None:
            custom = Custom.objects.filter(year=release)
        else:
            custom = Custom.objects.filter(type=collectibleType)
        if custom.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        custom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormsList(APIView):
    def get(self, request, format=None):
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FormsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormsDetails(APIView):
    def get(self, request, name=None, id=None, format=None):
        if(name != None):
            forms = Forms.objects.filter(collection_name=name)
        else:
            forms = Forms.objects.filter(collectible_id=id)
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)

    def put(self, request, name=None, id=None, format=None):
        if(name != None):
            forms = Forms.objects.filter(collection_name=name).first()
        else:
            forms = Forms.objects.filter(collectible_id=id).first()
        serializer = FormsSerializer(forms, data=request.data)
        print(forms)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name=None, id=None, format=None):
        if(name != None):
            forms = Forms.objects.filter(collection_name=name)
        else:
            forms = Forms.objects.filter(collectible_id=id)
        if forms.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        forms .delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MadeOfList(APIView):
    def get(self, request, format=None):
        madeOf = Made_Of.objects.all()
        serializer = MadeOfSerializer(madeOf, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MadeOfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MadeOfDetails(APIView):
    def get(self, request, oID=None, id=None, format=None):
        if oID != None:
            madeOf = Made_Of.objects.filter(order_id=oID)
        else:
            madeOf = Made_Of.objects.filter(collectible_id=id)
        serializer = MadeOfSerializer(madeOf, many=True)
        return Response(serializer.data)

    def put(self, request, oID=None, id=None, format=None):
        if oID != None:
            madeOf = Made_Of.objects.filter(order_id=oID).first()
        else:
            madeOf = Made_Of.objects.filter(collectible_id=id).first()
        serializer = MadeOfSerializer(madeOf, data=request.data)
        print(madeOf)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, oID=None, id=None, format=None):
        if oID != None:
            madeOf = Made_Of.objects.filter(order_id=oID)
        else:
            madeOf = Made_Of.objects.filter(collectible_id=id)
        if madeOf.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        madeOf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetails(APIView):
    def get(self, request, pk=None, user=None, format=None):
        if(pk != None):
            order = Order.objects.filter(pk=pk)
        else:
            order = Order.objects.filter(userName=user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None, user=None, format=None):
        if(pk != None):
            order = Order.objects.filter(pk=pk).first()
        else:
            order = Order.objects.filter(userName=user).first()
        serializer = OrderSerializer(order, data=request.data)
        print(order)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, user=None, format=None):
        if(pk != None):
            order = Order.objects.filter(pk=pk)
        else:
            order = Order.objects.filter(userName=user)
        if order.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FulfillsList(APIView):
    def get(self, request, format=None):
        fulfills = Fulfills.objects.all()
        serializer = FulfillsSerializer(fulfills, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FulfillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FulfillsDetails(APIView):
    def get(self, request, user=None, oID=None, format=None):
        if user != None:
            fulfills = Fulfills.objects.filter(userName=user)
        else:
            fulfills = Fulfills.objects.filter(orderID=oID)
        serializer = FulfillsSerializer(fulfills, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, oID=None, format=None):
        if user != None:
            fulfills = Fulfills.objects.filter(userName=user).first()
        else:
            fulfills = Fulfills.objects.filter(orderID=oID).first()
        serializer = FulfillsSerializer(fulfills, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, oID=None, format=None):
        if user != None:
            fulfills = Fulfills.objects.filter(userName=user)
        else:
            fulfills = Fulfills.objects.filter(orderID=oID)
        if fulfills.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        fulfills.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentList(APIView):
    def get(self, request, format=None):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetails(APIView):
    def get(self, request, pk=None, oID=None, format=None):
        if pk != None:
            payment = Payment.objects.filter(pk=pk)
        else:
            payment = Payment.objects.filter(orderID=oID)
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None, oID=None, format=None):
        if pk != None:
            payment = Payment.objects.filter(pk=pk).first()
        else:
            payment = Payment.objects.filter(orderID=oID).first()
        serializer = PaymentSerializer(payment, data=request.data)
        print(payment)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, oID=None, format=None):
        if pk != None:
            payment = Payment.objects.filter(pk=pk)
        else:
            payment = Payment.objects.filter(orderID=oID)
        if payment.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShippingMethodList(APIView):
    def get(self, request, format=None):
        shipping = Shipping_Method.objects.all()
        serializer = ShippingMethodSerializer(shipping, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShippingMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShippingMethodDetail(APIView):

    def get(self, request, user=None, method=None, format=None):
        if user != None and method != None:
            shipping = Shipping_Method.objects.filter(username=user, shippingMethod=method)
        elif user!= None:
            shipping = Shipping_Method.objects.filter(username=user)
        else:
            shipping = Shipping_Method.objects.filter(shippingMethod=method)
        serializer = ShippingMethodSerializer(shipping, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, method=None, format=None):
        if user != None and method != None:
            shipping = Shipping_Method.objects.filter(username=user, shippingMethod=method).first()
        elif user!= None:
            shipping = Shipping_Method.objects.filter(username=user).first()
        else:
            shipping = Shipping_Method.objects.filter(shippingMethod=method).first()
        serializer = ShippingMethodSerializer(shipping, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, method=None, format=None):
        if user != None and method != None:
            shipping = Shipping_Method.objects.filter(username=user, shippingMethod=method)
        elif user!= None:
            shipping = Shipping_Method.objects.filter(username=user)
        else:
            shipping = Shipping_Method.objects.filter(shippingMethod=method)
        if shipping.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        shipping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WarehouseList(APIView):
    def get(self, request, format=None):
        warehouse = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseDetail(APIView):

    def get(self, request, id=None, user=None, format=None):
        if id != None:
            warehouse = Warehouse.objects.filter(warehouseNumber=id)
        else:
            warehouse = Warehouse.objects.filter(username=user)
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, user=None, format=None):
        if id != None:
            warehouse = Warehouse.objects.filter(warehouseNumber=id).first()
        else:
            warehouse = Warehouse.objects.filter(username=user).first()
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, user=None, format=None):
        if id != None:
            warehouse = Warehouse.objects.filter(warehouseNumber=id)
        else:
            warehouse = Warehouse.objects.filter(username=user)
        if warehouse.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ModeratesList(APIView):
    def get(self, request, format=None):
        moderates = Moderates.objects.all()
        serializer = ModeratesSerializer(moderates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ModeratesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModeratesDetail(APIView):

    def get(self, request, user, format=None):
        moderates = Moderates.objects.filter(username=user)
        serializer = ModeratesSerializer(moderates, many=True)
        return Response(serializer.data)

    def put(self, request, user, format=None):
        moderates = Moderates.objects.filter(username=user).first()
        serializer = ModeratesSerializer(moderates, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user, format=None):
        moderates = Moderates.objects.filter(username=user)
        if moderates.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        moderates.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCollectionList(APIView):
    def get(self, request, format=None):
        collection = UserCollection.objects.all()
        serializer = UserCollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCollectionDetail(APIView):

    def get(self, request, name=None, user=None, format=None):
        if name != None and user != None:
            collection = UserCollection.objects.filter(collectionName=name, userName=user)
        elif name != None:
            collection = UserCollection.objects.filter(collectionName=name)
        else:
            collection = UserCollection.objects.filter(userName=user)
        serializer = UserCollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def put(self, request, name=None, user=None, format=None):
        if name != None and user != None:
            collection = UserCollection.objects.filter(collectionName=name, userName=user).first()
        elif name != None:
            collection = UserCollection.objects.filter(collectionName=name).first()
        else:
            collection = UserCollection.objects.filter(userName=user).first()
        serializer = UserCollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name=None, user=None, format=None):
        if name != None and user != None:
            collection = UserCollection.objects.filter(collectionName=name, userName=user)
        elif name != None:
            collection = UserCollection.objects.filter(collectionName=name)
        else:
            collection = UserCollection.objects.filter(userName=user)
        if collection.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsistsOfList(APIView):
    def get(self, request, format=None):
        consist = Consists_Of.objects.all()
        serializer = ConsistsOfSerializer(consist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConsistsOfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsistsOfDetail(APIView):

    def get(self, request, id=None, name=None, format=None):
        if id != None and name != None:
            collections = UserCollection.objects.filter(collectionName=name)
            data = []
            for collection in collections:
                consist = Consists_Of.objects.filter(collectionName=collection.id, collectible_id=id)
                print(consist)
                serializer = ConsistsOfSerializer(consist, many=True)
                data += serializer.data
            return Response(data)
        elif id != None:
            consist = Consists_Of.objects.filter(collectible_id=id)
        else:
            collections = UserCollection.objects.filter(collectionName=name)
            data = []
            for collection in collections:
                consist = Consists_Of.objects.filter(collectionName=collection.id)
                print(consist)
                serializer = ConsistsOfSerializer(consist, many=True)
                data += serializer.data
            return Response(data)
        serializer = ConsistsOfSerializer(consist, many=True)
        return Response(serializer.data)

    def put(self, request, id, name, format=None):
        collections = UserCollection.objects.filter(collectionName=name)
        consist = Consists_Of.objects.filter(collectionName=collections[0].id, collectible_id=id).first()
        serializer = ConsistsOfSerializer(consist, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, name, format=None):
        collection = UserCollection.objects.filter(collectionName=name).first()
        if collection == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consist = Consists_Of.objects.filter(collectionName=collection.id, collectible_id=id)
        if consist.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellsList(APIView):
    def get(self, request, format=None):
        sell = Sells.objects.all()
        serializer = SellsSerializer(sell, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SellsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellsDetail(APIView):

    def get(self, request, id=None, user=None, format=None):
        if id != None and user != None:
            sells = Sells.objects.filter(collectible_id=id, username=user)
        elif id != None:
            sells = Sells.objects.filter(collectible_id=id).order_by('price')
        else:
            sells = Sells.objects.filter(username=user)
        serializer = SellsSerializer(sells, many=True)
        return Response(serializer.data)

    def put(self, request, id, user, format=None):
        sells = Sells.objects.filter(collectible_id=id, username=user).first()
        serializer = SellsSerializer(sells, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, user=None, format=None):
        sells = Sells.objects.filter(collectible_id=id, username=user)
        if sells.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sells.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WantsList(APIView):
    def get(self, request, format=None):
        wants = Wants.objects.all()
        serializer = WantsSerializer(wants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WantsDetail(APIView):

    def get(self, request, user=None, name=None, format=None):
        if user != None and name != None:
            wants = Wants.objects.filter(userName=user, collectionName=name)
        elif user != None:
            wants = Wants.objects.filter(userName=user)
        else:
            wants = Wants.objects.filter(collectionName=name)
        serializer = WantsSerializer(wants, many=True)
        return Response(serializer.data)

    def put(self, request, user, name, format=None):
        wants = Wants.objects.filter(userName=user, collectionName=name).first()
        serializer = WantsSerializer(wants, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user, name, format=None):
        wants = Wants.objects.filter(userName=user, collectionName=name)
        if wants.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        wants.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):
    def get(self, request, format=None):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionDetail(APIView):

    def get(self, request, name, format=None):
        collection = Collection.objects.get(collection_name=name)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        collection = Collection.objects.filter(collection_name=name).first()
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        collection = Collection.objects.filter(collection_name=name)
        if collection.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagesList(APIView):
    def get(self, request, format=None):
        manages = Manages.objects.all()
        serializer = ManagesSerializer(manages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ManagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagesDetail(APIView):

    def get(self, request, id=None, user=None, format=None):
        if id != None and user != None:
            manages = Manages.objects.filter(collectible_id=id, adminUsername=user)
        elif id != None:
            manages = Manages.objects.filter(collectible_id=id)
        else:
            manages = Manages.objects.filter(adminUsername=user)
        serializer = ManagesSerializer(manages, many=True)
        return Response(serializer.data)

    def put(self, request, id, user, format=None):
        manages = Manages.objects.filter(
            collectible_id=id, adminUsername=user).first()
        serializer = ManagesSerializer(manages, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        manages = Manages.objects.filter(collectible_id=id, adminUsername=user)
        if manages.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        manages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminList(APIView):
    def get(self, request, format=None):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetail(APIView):
    def get(self, request, user, format=None):
        admin = Admin.objects.filter(userName=user)
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)
    
    def put(self, request, user, format=None):
        admin = Admin.objects.filter(userName=user).first()
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user, format=None):
        admin = Admin.objects.filter(userName=user)
        if admin.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DealsWithList(APIView):
    def get(self, request, format=None):
        deal = Deals_With.objects.all()
        serializer = DealsWithSerializer(deal, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DealsWithSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealsWithDetail(APIView):

    def get(self, request, id=None, user=None, format=None):
        if id != None:
            deal = Deals_With.objects.get(orderID=id)
        else:
            deal = Deals_With.objects.get(adminUsername=user)
        serializer = DealsWithSerializer(deal)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        deal = Deals_With.objects.filter(orderID=id).first()
        serializer = DealsWithSerializer(deal, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deal = Deals_With.objects.filter(orderID=id)
        if deal.first() == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
