from django.urls import path
from . import views

urlpatterns = [
    # List clients
    path('clients/', views.ClientList.as_view()),

    # List collectors/sellers
    path('clients/collectors/', views.CollectorList().as_view()),
    path('clients/sellers/', views.SellerList().as_view()),

    # Searching clients
    path('search/clients/', views.ClientList.as_view()),
    path('search/clients/<str:user>', views.ClientDetail.as_view()),
    path('search/clients/name/<str:clientname>', views.ClientDetail.as_view()),
    path('search/clients/phone/<str:num>', views.ClientDetail.as_view()),
    path('search/clients/collectors/<str:user>',
         views.CollectorDetail().as_view()),
    path('search/clients/sellers/<str:user>', views.SellerDetail().as_view()),
    path('search/clients/collectors/name/<str:clientname>',
         views.CollectorDetail().as_view()),
    path('search/clients/sellers/name/<str:clientname>',
         views.SellerDetail().as_view()),
    path('search/clients/collectors/phone/<str:num>',
         views.CollectorDetail().as_view()),
    path('search/clients/sellers/phone/<str:num>',
         views.SellerDetail().as_view()),

    # List all collectibles
    path('collectibles/', views.CollectibleList.as_view()),

    # List albums
    path('collectibles/albums/', views.AlbumList.as_view()),

    # Searching albums
    path('search/collectibles/albums/', views.AlbumList.as_view()),
    path('search/collectibles/albums/<int:id>', views.AlbumDetail.as_view()),
    path('search/collectibles/albums/<str:albumName>',
         views.AlbumDetail.as_view()),
    path('search/collectibles/albums/type/<str:albumType>',
         views.AlbumDetail.as_view()),
    path('search/collectibles/albums/artist/<str:artistName>',
         views.AlbumDetail.as_view()),
    path('search/collectibles/albums/releaseyear/<int:release>',
         views.AlbumDetail.as_view()),

    # List all comic books
    path('collectibles/comicBooks/', views.ComicBookList.as_view()),

    # Searching comic books
    path('search/collectibles/comicBooks/',
         views.ComicBookList.as_view()),
    path('search/collectibles/comicBooks/<int:id>',
         views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/<str:comicName>',
         views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/author/<str:authorName>',
         views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/illustrator/<str:illustratorName>',
         views.ComicBookDetails.as_view()),
    path('search/collectibles/comicBooks/releaseyear/<int:release>',
         views.ComicBookDetails.as_view()),

    # List all sport cards
    path('collectibles/sportCards/', views.SportCardList.as_view()),

    # Searching sport cards
    path('search/collectibles/sportCards/<int:id>',
         views.SportCardDetails.as_view()),
    path('search/collectibles/sportCards/<str:cardName>',
         views.SportCardDetails.as_view()),
    path('search/collectibles/sportCards/type/<str:cardType>',
         views.SportCardDetails.as_view()),
    path('search/collectibles/sportCards/sport/<str:sportName>',
         views.SportCardDetails.as_view()),
    path('search/collectibles/sportCards/releaseyear/<int:release>',
         views.SportCardDetails.as_view()),

    # Listing all custom collectibles
    path('collectibles/custom/', views.CustomList.as_view()),

    # Searching custom collectibles
    path('search/collectibles/custom/<int:id>', views.CustomDetails.as_view()),
    path('search/collectibles/custom/<str:collectibleName>',
         views.CustomDetails.as_view()),
    path('search/collectibles/custom/type/<str:collectibleType>',
         views.CustomDetails.as_view()),

    # Listing all form relations
    path('collectibles/forms/', views.FormsList.as_view()),

    # Searching forms
    path('search/collectibles/forms/', views.FormsList.as_view()),
    path('search/collectibles/forms/<int:id>', views.FormsDetails.as_view()),
    path('search/collectibles/forms/<str:name>', views.FormsDetails.as_view()),

    # Listing all made of relations
    path('order/madeOf/', views.MadeOfList.as_view()),

    # Searching made of
    path('search/order/madeOf/<int:oID>', views.MadeOfDetails.as_view()),
    path('search/order/madeOf/collectibles/<int:id>',
         views.MadeOfDetails.as_view()),

    # Listing all orders
    path('order/', views.OrderList.as_view()),

    #Searching orders
    path('search/order/<int:pk>', views.OrderDetails.as_view()),
    path('search/order/<str:user>', views.OrderDetails.as_view()),
    path('search/order/', views.OrderList.as_view()),

    # Searching fulfills
    path('order/fulfills/', views.FulfillsList.as_view()),
    path('search/order/fulfills/<int:oID>',
         views.FulfillsDetails.as_view()),
     path('search/order/fulfills/<str:user>',
         views.FulfillsDetails.as_view()),
    path('search/order/fulfills/<int:oID>/<str:user>',
         views.FulfillsDetails.as_view()),

    # List all payments
    path('payment/', views.PaymentList.as_view()),

    #Searching payments
    path('search/payment/<int:pk>', views.PaymentDetails.as_view()),
    path('search/payment/order/<int:oID>', views.PaymentDetails.as_view()),

    # List all warehouses
    path('warehouse/', views.WarehouseList.as_view()),

    # Searching warehouses
    path('search/warehouse/<int:id>', views.WarehouseDetail.as_view()),
    path('search/warehouse/<str:user>', views.WarehouseDetail.as_view()),

    # List all shipping methods
    path('shipping_method/', views.ShippingMethodList.as_view()),

    # Searching shipping methods
    path('search/shipping_method/<str:user>',
         views.ShippingMethodDetail.as_view()),
    path('search/shipping_method/method/<str:method>',
         views.ShippingMethodDetail.as_view()),

    # List all moderates relations
    path('moderates/', views.ModeratesList.as_view()),

    # Searching moderates relations
    path('search/moderates/<str:user>',
         views.ModeratesDetail.as_view()),

    # Listing user collections
    path('user_collection/', views.UserCollectionList.as_view()),

    # Searching user collections
    path('search/user_collection/<str:user>',
         views.UserCollectionDetail.as_view()),
    path('search/user_collection/name/<str:name>',
         views.UserCollectionDetail.as_view()),

    # Listing all consists of relations
    path('consists_of/', views.ConsistsOfList.as_view()),

    #Searching consists of relations
    path('search/consists_of/<int:id>/<str:user>',
         views.ConsistsOfDetail.as_view()),

    #Listing all sells relations
    path('sells/', views.SellsList.as_view()),
    path('search/sells/<int:id>',
         views.SellsDetail.as_view()),
    path('search/sells/<str:user>',
         views.SellsDetail.as_view()),

    #Listing all wants relations
    path('wants/', views.WantsList.as_view()),

    #Searching all wants
    path('search/wants/<str:user>',
         views.WantsDetail.as_view()),
    path('search/wants/collection/<str:name>',
         views.WantsDetail.as_view()),

    #Listing all collections
    path('collections/', views.CollectionList.as_view()),

    #Searching all collections
    path('search/collections/<str:name>', views.CollectionDetail.as_view()),

    #Listing all manages relations
    path('manages/', views.ManagesList.as_view()),
    #Searching manages relations
    path('search/manages/<int:id>/<str:user>',
         views.ManagesDetail.as_view()),

    #Listing admins
    path('api/admin/', views.AdminList.as_view()),

    #Listing all dealsWith relations
    path('dealsWith/', views.DealsWithList.as_view()),

    #Searching dealsWith relations
    path('search/dealsWith/<int:id>', views.DealsWithDetail.as_view()),
]
