from django.urls import path,include
from . import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>', views.ClientDetail.as_view()),
    path('collectibles/albums/', views.AlbumList.as_view()),
]