from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework.fields import SerializerMethodField

from . import models

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class SongPairingSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.SongPairing
        fields = '__all__'
class SongValuesSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.SongValues
        fields = '__all__'
