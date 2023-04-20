from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import User, SongPairing, SongValues

import json
import os
import spotipy

from . import serializers
from .login import login, check_current_user_match
from .auto_queue import auto_queue

def index(request):
    return HttpResponse("Hi")

def get_current_song(request):
    login(request)
    cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
    if (cache_token is not None):
        sp = spotipy.Spotify(cache_token['access_token'])
        if (sp.currently_playing() is not None):
            cur_song = sp.currently_playing()['item']['external_urls']['spotify']
            if cur_song is not None:
                return HttpResponse(cur_song)
        return HttpResponse("No song playing")
                
    else:
        return Response(status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

@api_view(("POST",))
def compare_songs(request):
    login(request)
    cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
    if cache_token is not None:
        try:
            client_song = json.loads(request.body)['current']
            sp = spotipy.Spotify(cache_token['access_token'])
            cur_song = sp.currently_playing()['item']['external_urls']['spotify']
            if client_song != cur_song:
                auto_queue(request)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'new_song' : cur_song})
    else:
        return Response(status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

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

    def put(self, request, pk, *args, **kwargs):
        login(request)
        cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
        if check_current_user_match(spotipy.Spotify(cache_token['access_token']), pk):
            return self.update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

    def get(self, request, pk, *args, **kwargs):
        login(request)
        cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
        if check_current_user_match(spotipy.Spotify(cache_token['access_token']), pk):
            return self.retrieve(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
    
    def delete(self, request, pk, *args, **kwargs):
        login(request)
        cache_token = spotipy.DjangoSessionCacheHandler(request).get_cached_token()
        if check_current_user_match(spotipy.Spotify(cache_token['access_token']), pk):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
        
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
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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