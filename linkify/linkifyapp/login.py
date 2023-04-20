import spotipy
from .views import User
import os

client_id = os.environ.get('LINKIFY_CLIENT_ID')
client_secret = os.environ.get('LINKIFY_SECRET')
redirect_uri = 'http://localhost:8888/callback'

def login(request):
    cache_handler = spotipy.DjangoSessionCacheHandler(request)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state', cache_handler=cache_handler)
    if auth_manager.validate_token(cache_handler.get_cached_token()):
        sp = spotipy.Spotify(cache_handler.get_cached_token()['access_token'])
        check_if_user_exists(sp)
        return None
    cache_handler.save_token_to_cache(auth_manager.get_access_token())
    sp = spotipy.Spotify(cache_handler.get_cached_token()['access_token'])
    check_if_user_exists(sp)
    return None

def check_if_user_exists(sp):
    id= sp.me()['id']
    name = sp.me()['display_name']
    if not User.objects.filter(id=id,username=name).exists():
        u = User(id=id,username=name)
        u.save()