from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters

import os
import spotipy

from . import serializers

client_id = os.environ.get('LINKIFY_CLIENT_ID')
client_secret = os.environ.get('LINKIFY_SECRET')
redirect_uri = 'http://localhost:9090/callback'
token = None

def index(request):
    return HttpResponse("Hi")

def login_test(request):
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state')
    auth_url = auth_manager.get_authorize_url()
    
    return redirect(auth_url)
    

def get_current_song(request):
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state')
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return HttpResponse(sp.currently_playing()['item']['external_urls']['spotify'])


class UserView(generics.ListCreateAPIView):
    pass
