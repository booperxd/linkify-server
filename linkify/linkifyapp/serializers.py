from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from . import models

class UserSerializer(serializers.ModelSerializer):
    metadata = SerializerMethodField()

    class Meta:
        model = models.User
        fields = ["id", "username", "song_pairings"]

    def get_metadata(self, obj):
        return obj.metadata

class SongPairingSerializer(serializers.ModelSerializer):
    metadata = SerializerMethodField()

    class Meta:
        model = models.SongPairing
        fields = ["id", "song_key", "song_values"]

    def get_metadata(self, obj):
        return obj.metadata