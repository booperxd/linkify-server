import os
import spotipy
import spotipy.client
from spotipy.oauth2 import SpotifyOAuth

test_dict = {'https://open.spotify.com/track/4CJ7iadNL15GuTr7fXMqxr' : ['https://open.spotify.com/track/1BcuFfskHNf1WvqpyCs4wT', 'https://open.spotify.com/track/37wXJXAHLBxOcGdwMaFbEb']}

client_id = os.environ.get('LINKIFY-CLIENT-ID')
client_secret = os.environ.get('LINKIFY-SECRET')
redirect_uri = 'http://127.0.0.1:9090'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope = 'user-read-currently-playing user-modify-playback-state user-read-playback-state'))

#spotipy does not support clearing queues. unfortunate.
def get_old_queue():
    queue = sp.queue()


def add_song_to_queue(song_url):
    sp.add_to_queue(song_url)

def add_all_songs_to_queue(songs):
    for song in songs:
        add_song_to_queue(song)

def check_current_song(cur_song):
    if cur_song in test_dict:
        add_all_songs_to_queue(test_dict[cur_song])

cur_song = None

while True:
    new_song = sp.currently_playing()['item']['external_urls']['spotify']
    if cur_song != new_song:
        print('song changed!')
        check_current_song(new_song)
    cur_song = new_song

def junk():
    cur_song = sp.currently_playing()['item']['external_urls']['spotify']
    queue = sp.queue()['queue']
    #print(queue[0]['external_urls']['spotify'])
    for i in range(0, len(queue)):
        print(queue[i]['name'])
        print(queue[i]['external_urls']['spotify'])
    
    else:
        print('nope!')
