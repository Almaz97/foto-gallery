from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import AlbumSerializer, TopAlbumViewSerializer
from .models import Album


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views += 1
        obj.save()
        return super().retrieve(obj, request, *args, **kwargs)


class TopAlbumsView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    def get(self, request):
        top_albums = Album.objects.all().order_by('-views')[:10]
        serializer = TopAlbumViewSerializer(
            instance=top_albums, many=True, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
