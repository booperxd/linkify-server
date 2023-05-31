import spotipy
from .views import User
import os

client_id = os.environ.get('LINKIFY_CLIENT_ID')
client_secret = os.environ.get('LINKIFY_SECRET')
redirect_uri = 'http://localhost:8888/callback'

def login(request):
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state')
    token = auth_manager.get_access_token()['access_token']
    sp = spotipy.Spotify(auth_manager=auth_manager)
    check_if_user_exists(sp)
    cur_user = User.objects.get(id = sp.me()['id'])
    cur_user.token = token
    cur_user.save()
    request.user = cur_user

def check_if_user_exists(sp):
    id= sp.me()['id']
    name = sp.me()['display_name']
    if not User.objects.filter(id=id,username=name).exists():
        u = User(id=id,username=name)
        u.save()

def check_authenticated(request):
    try:
        token = request.user.token
    except:
        token = None
    if token is not None or (spotipy.Spotify(token) == True):
        return True
    else:
        login(request)
        if request.user.token is None:
            return False
        else:
            return True
    