from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import AlbumViewSet, TopAlbumsView

router = routers.SimpleRouter()

router.register('albums', AlbumViewSet, 'albums')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/top_album_views/', TopAlbumsView.as_view(), name='top-views')
]