import spotipy
from .login import login
from .views import User

def auto_queue(request, token):
    if token is not None:
        try:
            sp = spotipy.Spotify(token)
            id = sp.me()['id']
            cur_user = User.objects.get(id = id)
            cur_song = sp.currently_playing()['item']['external_urls']['spotify']
            songs = cur_user.song_pairings.get(song_key=cur_song).song_values.all()
            for song in songs:
                sp.add_to_queue(song.song_uri)
            return cur_song
        except:
            return None
    return None