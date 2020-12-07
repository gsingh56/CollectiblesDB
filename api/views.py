from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.
class ClientList (APIView):
    def get(self, request, format=None):
        print(request)
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
        serializer = ClientSerializer(client, many=True)
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
        serializer = ClientSerializer(client, data=request.data)
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
        serializer = ClientSerializer(sellers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
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
            comicBook = ComicBook.objects.filter(illustrator=illustratorName).first()
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
            album = Album.objects.filter(type=albumType).first()
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
        serializer = SportCardSerializer(sport)
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

    def get(self, request, pk, format=None):
        custom = Custom.objects.get(pk=pk)
        serializer = CustomSerializer(custom)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        custom = Custom.objects.filter(pk=pk).first()
        serializer = CustomSerializer(custom, data=request.data)
        print(custom)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        custom = Custom.objects.filter(pk=pk)
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


class formsDetails(APIView):
    def get(self, request, pk, format=None):
        forms = Forms.objects.get(pk=pk)
        serializer = FormsSerializer(forms)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        forms = Forms.objects.filter(pk=pk).first()
        serializer = FormsSerializer(forms, data=request.data)
        print(forms)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        forms = Forms.objects.filter(pk=pk)
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
    def get(self, request, pk, format=None):
        madeOf = Made_Of.objects.get(pk=pk)
        serializer = MadeOfSerializer(madeOf)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        madeOf = Made_Of.objects.filter(pk=pk).first()
        serializer = MadeOfSerializer(madeOf, data=request.data)
        print(madeOf)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        madeOf = Made_Of.objects.filter(pk=pk)
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


class OrderListDetails(APIView):
    def get(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(order, data=request.data)
        print(order)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = Order.objects.filter(pk=pk)
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
    def get(self, request, pk, userName, orderID, format=None):
        fulfills = Fulfills.objects.get(
            pk=pk, userName=userName, orderID=orderID)
        serializer = FulfillsSerializer(fulfills)
        return Response(serializer.data)

    def put(self, request, pk, userName, orderID, format=None):
        fulfills = Fulfills.objects.filter(
            pk=pk, userName=userName, orderID=orderID).first()
        serializer = FulfillsSerializer(fulfills, data=request.data)
        print(fulfills)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, userName, orderID, format=None):
        fulfills = Fulfills.objects.filter(
            pk=pk, userName=userName, orderID=orderID)
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
    def get(self, request, pk, format=None):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment = Payment.objects.filter(pk=pk).first()
        serializer = PaymentSerializer(payment, data=request.data)
        print(payment)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment = Payment.objects.filter(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShippingMethodList(APIView):
    def get(self, request, format=None):
        shipping = Shipping_Method.objects.all()
        serializer = ShippingMethodSerializer(shipping, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ShippingMethodSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingMethodDetail(APIView):

    def get(self, request, id, user, format=None):
        shipping = Shipping_Method.objects.get (userID=id, userName=user)
        serializer = ShippingMethodSerializer(shipping)
        return Response (serializer.data)

    def put(self, request, id, user, format=None):
        shipping = Shipping_Method.objects.filter(userID=id, userName=user).first()
        serializer = ShippingMethodSerializer(shipping, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        shipping = Shipping_Method.objects.filter(userID=id, userName=user)
        shipping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WarehouseList(APIView):
    def get(self, request, format=None):
        warehouse = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseListUser(APIView):
    def get(self, request, id, format=None):
        warehouse = Warehouse.objects.filter(userID=id)
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseDetail(APIView):

    def get(self, request, id, format=None):
        warehouse = Warehouse.objects.get (warehouseNumber=id)
        serializer = WarehouseSerializer(warehouse)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        warehouse = Warehouse.objects.filter(warehouseNumber=id).first()
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        warehouse = Warehouse.objects.filter(warehouseNumber=id)
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ModeratesList(APIView):
    def get(self, request, format=None):
        moderates = Moderates.objects.all()
        serializer = WarehouseSerializer(moderates, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ModeratesSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModeratesDetail(APIView):

    def get(self, request, id, user, format=None):
        moderates = Moderates.objects.get (userID=id, userName=user)
        serializer = ModeratesSerializer(moderates)
        return Response (serializer.data)

    def put(self, request, id, user, format=None):
        moderates = Moderates.objects.filter(userID=id, userName=user).first()
        serializer = ModeratesSerializer(moderates, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        moderates = Moderates.objects.filter(userID=id, userName=user)
        moderates.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCollectionList(APIView):
    def get(self, request, format=None):
        collection = UserCollection.objects.all()
        serializer = UserCollectionSerializer(collection, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserCollectionSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCollectionDetail(APIView):

    def get(self, request, id, user, format=None):
        collection = UserCollection.objects.get (userID=id, userName=user)
        serializer = UserCollectionSerializer(collection)
        return Response (serializer.data)

    def put(self, request, id, user, format=None):
        collection = UserCollection.objects.filter(userID=id, userName=user).first()
        serializer = UserCollectionSerializer(collection, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        collection = UserCollection.objects.filter(userID=id, userName=user)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsistsOfList(APIView):
    def get(self, request, format=None):
        consist = Consists_Of.objects.all()
        serializer = ConsistsOfSerializer(consist, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ConsistsOfSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsistsOfDetail(APIView):

    def get(self, request, id, userid, format=None):
        consist = Consists_Of.objects.get (userID=userid, ID=id)
        serializer = ConsistsOfSerializer(consist)
        return Response (serializer.data)

    def put(self, request, id, userid, format=None):
        consist = Consists_Of.objects.filter(userID=userid, ID=id).first()
        serializer = ConsistsOfSerializer(consist, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, userid, format=None):
        consist = Consists_Of.objects.filter(userID=userid, ID=id)
        consist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SellsList(APIView):
    def get(self, request, format=None):
        sell = Sells.objects.all()
        serializer = SellsSerializer(sell, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SellsSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellsDetail(APIView):

    def get(self, request, id, userid, user, format=None):
        sells = Sells.objects.get (userID=userid, ID=id, userName=user)
        serializer = SellsSerializer(sells)
        return Response (serializer.data)

    def put(self, request, id, userid, user, format=None):
        sells = Sells.objects.filter(userID=userid, ID=id, userName=user).first()
        serializer = SellsSerializer(sells, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, userid, user, format=None):
        sells = Sells.objects.filter(userID=userid, ID=id, userName=user)
        sells.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WantsList(APIView):
    def get(self, request, format=None):
        wants = Wants.objects.all()
        serializer = WantsSerializer(wants, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WantsSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WantsDetail(APIView):

    def get(self, request, id, user, format=None):
        wants = Wants.objects.get (userID=id, userName=user)
        serializer = WantsSerializer(wants)
        return Response (serializer.data)

    def put(self, request, id, user, format=None):
        wants = Wants.objects.filter(userID=id, userName=user).first()
        serializer = WantsSerializer(wants, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        wants = Wants.objects.filter(userID=id, userName=user)
        wants.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(APIView):
    def get(self, request, format=None):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollectionDetail(APIView):

    def get(self, request, pk, format=None):
        collection = Collection.objects.get (pk=pk)
        serializer = CollectionSerializer(collection)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        collection = Collection.objects.filter(pk=pk).first()
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        collection = Collection.objects.filter(pk=pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ManagesList(APIView):
    def get(self, request, format=None):
        manages = Manages.objects.all()
        serializer = ManagesSerializer(manages, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ManagesSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagesDetail(APIView):

    def get(self, request, id, user, format=None):
        manages = Manages.objects.get (ID=id, adminUserName=user)
        serializer = ManagesSerializer(manages)
        return Response (serializer.data)

    def put(self, request, id, user, format=None):
        manages = Manages.objects.filter(ID=id, adminUserName=user).first()
        serializer = ManagesSerializer(manages, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, user, format=None):
        manages = Manages.objects.filter(ID=id, adminUserName=user)
        manages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminList(APIView):
    def get(self, request, format=None):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user, format=None):
        admin = Admin.objects.filter(userName=user).first()
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealsWithList(APIView):
    def get(self, request, format=None):
        deal = Deals_With.objects.all()
        serializer = DealsWithSerializer(deal, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DealsWithSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealsWithDetail(APIView):

    def get(self, request, id, format=None):
        deal = Deals_With.objects.get (orderID=id)
        serializer = DealsWithSerializer(deal)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        deal = Deals_With.objects.filter(orderID=id).first()
        serializer = DealsWithSerializer(deal, data=request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deal = Deals_With.objects.filter(orderID=id)
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)