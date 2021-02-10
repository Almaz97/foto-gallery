from rest_framework.viewsets import ModelViewSet
from .serializers import AlbumSerializer
from .models import Album


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
