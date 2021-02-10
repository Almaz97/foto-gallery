from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'user', 'title', 'image', 'created_at']

        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }
