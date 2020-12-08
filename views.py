from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.


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

    def get(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(userid=id, username=user)
        elif id != None:
            client = Client.objects.filter(userid=id)
        elif user != None:
            client = Client.objects.filter(username=user)
        elif clientname != None:
            client = Client.objects.filter(name=clientname)
        else:
            client = Client.objects.filter(phonenumber=num)
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(
                userid=id, username=user, cFlag=1).first()
        elif id != None:
            client = Client.objects.filter(
                userid=id, cFlag=1).first()
        elif user != None:
            client = Client.objects.filter(
                username=user, cFlag=1).first()
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname, cFlag=1).first()
        else:
            client = Client.objects.filter(
                phonenumber=num, cFlag=1).first()
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(
                userid=id, username=user, cFlag=1).first()
        elif id != None:
            client = Client.objects.filter(
                userid=id, cFlag=1).first()
        elif user != None:
            client = Client.objects.filter(
                username=user, cFlag=1).first()
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname, cFlag=1).first()
        else:
            client = Client.objects.filter(
                phonenumber=num, cFlag=1).first()
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

    def get(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(userid=id, username=user, cFlag=1)
        elif id != None:
            client = Client.objects.filter(userid=id, cFlag=1)
        elif user != None:
            client = Client.objects.filter(username=user, cFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, cFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, cFlag=1)
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(
                userid=id, username=user, cFlag=1).first()
        elif id != None:
            client = Client.objects.filter(
                userid=id, cFlag=1).first()
        elif user != None:
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

    def delete(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(
                userid=id, username=user, cFlag=1)
        elif id != None:
            client = Client.objects.filter(
                userid=id, cFlag=1)
        elif user != None:
            client = Client.objects.filter(
                username=user, cFlag=1)
        elif clientname != None:
            client = Client.objects.filter(
                name=clientname, cFlag=1)
        else:
            client = Client.objects.filter(
                phonenumber=num, cFlag=1)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerDetail(APIView):

    def get(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(userid=id, username=user, sFlag=1)
        elif id != None:
            client = Client.objects.filter(userid=id, sFlag=1)
        elif user != None:
            client = Client.objects.filter(username=user, sFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1)
        serializer = SellerSerializer(client, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(userid=id, username=user, sFlag=1)
        elif id != None:
            client = Client.objects.filter(userid=id, sFlag=1)
        elif user != None:
            client = Client.objects.filter(username=user, sFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1)
        serializer = SellerSerializer(client, data=request.data)
        print(client)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, user=None, clientname=None, num=None, format=None):
        if id != None and user != None:
            client = Client.objects.filter(userid=id, username=user, sFlag=1)
        elif id != None:
            client = Client.objects.filter(userid=id, sFlag=1)
        elif user != None:
            client = Client.objects.filter(username=user, sFlag=1)
        elif clientname != None:
            client = Client.objects.filter(name=clientname, sFlag=1)
        else:
            client = Client.objects.filter(phonenumber=num, sFlag=1)
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
        collectibles = Collectible.objects.all()
        serializer = CollectibleSerializer(collectibles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollectibleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    def get(self, request, id=None, comicName=None, authorName=None, illustratorName=None, release=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id)
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName)
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName)
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
        else:
            comicBook = ComicBook.objects.filter(illustrator=illustratorName)
        serializer = ComicBookSerializer(comicBook, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, comicName=None, authorName=None, illustratorName=None, release=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id).first()
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName).first()
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName).first()
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
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

    def delete(self, request, id=None, comicName=None, authorName=None, illustratorName=None, release=None, format=None):
        if id != None:
            comicBook = ComicBook.objects.filter(id=id)
        elif comicName != None:
            comicBook = ComicBook.objects.filter(name=comicName)
        elif authorName != None:
            comicBook = ComicBook.objects.filter(author=authorName)
        elif release != None:
            comicBook = ComicBook.objects.filter(year=release)
        else:
            comicBook = ComicBook.objects.filter(illustrator=illustratorName)
        comicBook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComicGenreList(APIView):
    def get(self, request, format=None):
        comicGenre = ComicGenre.objects.all()
        serializer = ComicGenreSerializer(comicGenre, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComicGenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicGenreDetails(APIView):

    def get(self, request, pk, format=None):
        comicGenre = ComicGenre.objects.get(pk=pk)
        serializer = ComicGenreSerializer(comicGenre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comicGenre = ComicGenre.objects.filter(pk=pk).first()
        serializer = ComicGenreSerializer(comicGenre, data=request.data)
        print(comicGenre)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comicGenre = ComicGenre.objects.filter(pk=pk)
        comicGenre.delete()
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

    def get(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id)
        elif albumName != None:
            album = Album.objects.filter(name=albumName)
        elif artistName != None:
            album = Album.objects.filter(artist=artistName)
        elif albumType != None:
            album = Album.objects.filter(type=albumType)
        else:
            album = Album.objects.filter(year=release)
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id).first()
        elif albumName != None:
            album = Album.objects.filter(name=albumName).first()
        elif artistName != None:
            album = Album.objects.filter(artist=artistName).first()
        elif albumType != None:
            album = Album.objects.filter(type=albumType).first()
        else:
            album = Album.objects.filter(year=release).first()
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, albumName=None, artistName=None, release=None, albumType=None, format=None):
        if id != None:
            album = Album.objects.filter(id=id)
        elif albumName != None:
            album = Album.objects.filter(name=albumName)
        elif artistName != None:
            album = Album.objects.filter(artist=artistName)
        elif albumType != None:
            album = Album.objects.filter(type=albumType)
        else:
            album = Album.objects.filter(year=release)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumGenreList(APIView):
    def get(self, request, format=None):
        albumGenre = AlbumGenre.objects.all()
        serializer = AlbumGenreSerializer(albumGenre, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumGenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumGenreDetails(APIView):
    def get(self, request, pk, format=None):
        albumGenre = AlbumGenre.objects.get(pk=pk)
        serializer = AlbumGenreSerializer(albumGenre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        albumGenre = AlbumGenre.objects.filter(pk=pk).first()
        serializer = AlbumGenreSerializer(albumGenre, data=request.data)
        print(albumGenre)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        albumGenre = AlbumGenre.objects.filter(pk=pk)
        albumGenre.delete()
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

    def get(self, request, id=None, collectibleName=None, collectibleType=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id)
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName)
        else:
            custom = Custom.objects.filter(type=collectibleType)
        serializer = CustomSerializer(custom, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, collectibleName=None, collectibleType=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id).first()
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName).first()
        else:
            custom = Custom.objects.filter(type=collectibleType).first()
        serializer = CustomSerializer(custom, data=request.data)
        print(custom)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, collectibleName=None, collectibleType=None, format=None):
        if id != None:
            custom = Custom.objects.filter(id=id)
        elif collectibleName != None:
            custom = Custom.objects.filter(name=collectibleName)
        else:
            custom = Custom.objects.filter(type=collectibleType)
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
            madeOf = Made_Of.objects.filter(id=id)
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
            order = Order.objects.get(pk=pk)
        else:
            order = Order.objects.filter(userName=user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None, user=None, format=None):
        if(pk != None):
            order = Order.objects.get(pk=pk).first()
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
            order = Order.objects.get(pk=pk)
        else:
            order = Order.objects.filter(userName=user)
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
        if user != None and oID != None:
            fulfills = Fulfills.objects.filter(orderID=oID, userName=user)
        elif user != None:
            fulfills = Fulfills.objects.filter(userName=user)
        else:
            fulfills = Fulfills.objects.filter(orderID=oID)
        serializer = FulfillsSerializer(fulfills, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, oID=None, format=None):
        if user != None and oID != None:
            fulfills = Fulfills.objects.filter(orderID=oID, userName=user).first()
        elif user != None:
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
        if user != None and oID != None:
            fulfills = Fulfills.objects.filter(orderID=oID, userName=user)
        elif user != None:
            fulfills = Fulfills.objects.filter(userName=user)
        else:
            fulfills = Fulfills.objects.filter(orderID=oID)
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
        if user!= None:
            shipping = Shipping_Method.objects.filter(username=user)
        else:
            shipping = Shipping_Method.objects.filter(shippingMethod=method)
        serializer = ShippingMethodSerializer(shipping, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, method=None, format=None):
        if user!= None:
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
        if user!= None:
            shipping = Shipping_Method.objects.filter(username=user)
        else:
            shipping = Shipping_Method.objects.filter(shippingMethod=method)
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
        if name != None:
            collection = UserCollection.objects.filter(collectionName=name)
        else:
            collection = UserCollection.objects.filter(userName=user)
        serializer = UserCollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def put(self, request, name=None, user=None, format=None):
        if name != None:
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
        if name != None:
            collection = UserCollection.objects.filter(collectionName=name)
        else:
            collection = UserCollection.objects.filter(userName=user)
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

    def get(self, request, id, user, format=None):
        consist = Consists_Of.objects.filter(username=user, collectible_id=id)
        serializer = ConsistsOfSerializer(consist, many=True)
        return Response(serializer.data)

    def put(self, request, id, user, format=None):
        consist = Consists_Of.objects.filter(username=user, collectible_id=id).first()
        serializer = ConsistsOfSerializer(consist, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        consist = Consists_Of.objects.filter(username=user, collectible_id=id)
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
        if id != None:
            sells = Sells.objects.filter(collectible_id=id)
        else:
            sells = Sells.objects.filter(username=user)
        serializer = SellsSerializer(sells, many=True)
        return Response(serializer.data)

    def put(self, request, id=None, user=None, format=None):
        if id != None:
            sells = Sells.objects.filter(collectible_id=id).first()
        else:
            sells = Sells.objects.filter(username=user).first()
        serializer = SellsSerializer(sells, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, user=None, format=None):
        if id != None:
            sells = Sells.objects.filter(collectible_id=id)
        else:
            sells = Sells.objects.filter(username=user)
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
        if user != None:
            wants = Wants.objects.filter(userName=user)
        else:
            wants = Wants.objects.filter(collectionName=name)
        serializer = WantsSerializer(wants, many=True)
        return Response(serializer.data)

    def put(self, request, user=None, name=None, format=None):
        if user != None:
            wants = Wants.objects.filter(userName=user).first()
        else:
            wants = Wants.objects.filter(collectionName=name).first()
        serializer = WantsSerializer(wants, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user=None, name=None, format=None):
        if user != None:
            wants = Wants.objects.filter(userName=user)
        else:
            wants = Wants.objects.filter(collectionName=name)
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

    def get(self, request, id, user, format=None):
        manages = Manages.objects.get(collectible_id=id, adminUsername=user)
        serializer = ManagesSerializer(manages)
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

    def put(self, request, user, format=None):
        admin = Admin.objects.filter(userName=user).first()
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get(self, request, id, format=None):
        deal = Deals_With.objects.get(orderID=id)
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
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
