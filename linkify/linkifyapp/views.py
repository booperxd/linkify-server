from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters

from .models import User, SongPairing, SongValues

import os
import spotipy

from . import serializers

client_id = os.environ.get('LINKIFY_CLIENT_ID')
client_secret = os.environ.get('LINKIFY_SECRET')
redirect_uri = 'http://localhost:8888/callback'

def index(request):
    return HttpResponse("Hi")

def login_test(request):
    cache_handler = spotipy.DjangoSessionCacheHandler(request)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state', cache_handler=cache_handler)
    if auth_manager.validate_token(cache_handler.get_cached_token()):
        sp = spotipy.Spotify(cache_handler.get_cached_token()['access_token'])
        check_if_user_exists(sp)
        return cache_handler.get_cached_token()
    cache_handler.save_token_to_cache(auth_manager.get_access_token())
    sp = spotipy.Spotify(cache_handler.get_cached_token()['access_token'])
    check_if_user_exists(sp)
    return cache_handler.get_cached_token()

def check_if_user_exists(sp):
    id= sp.me()['id']
    name = sp.me()['display_name']
    if not User.objects.filter(id=id,username=name).exists():
        u = User(id=id,username=name)
        u.save()

def get_current_song(request):
    login_test(request)
    cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
    sp = spotipy.Spotify(cache_token['access_token'])
    return HttpResponse(sp.currently_playing()['item']['external_urls']['spotify'])


class UserView(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    search_fields = ['id', 'username']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
   

class SpecificUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class SongPairingView(generics.ListCreateAPIView):
    model = SongPairing
    queryset = SongPairing.objects.all()
    serializer_class = serializers.SongPairingSerializer
    search_fields = ['id', 'song_key']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SpecificSongPairingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SongPairing.objects.all()
    serializer_class = serializers.SongPairingSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class SongValuesView(generics.ListCreateAPIView):
    model = SongValues
    queryset = SongValues.objects.all()
    serializer_class = serializers.SongValuesSerializer
    search_fields = ['id', 'song_uri']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SpecificSongValuesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SongValues.objects.all()
    serializer_class = serializers.SongValuesSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)