from django.urls import path,include
from . import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:id>/<str:user>', views.ClientDetail.as_view()),
    path('collectibles/albums/', views.AlbumList.as_view()),
    path('collectibles/albums/<int:pk>', views.AlbumDetail.as_view()),
]