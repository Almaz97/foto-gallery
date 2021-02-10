from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Album


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'user', 'title', 'image', 'views', 'created_at']

        extra_kwargs = {
            'user': {
                'read_only': True
            },
            'views': {
                'read_only': True
            }
        }


class TopAlbumViewSerializer(AlbumSerializer):

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response
