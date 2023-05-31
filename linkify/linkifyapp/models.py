from django.db import models
#This might given an error. Refer to this https://stackoverflow.com/questions/70656495/importerror-cannot-import-name-ugettext-lazy
import jsonfield

# User model
#id = spotify id
#username = spotify display name
#song_pairings = [1, 4, 69]
class User(models.Model):
    id = models.CharField(max_length = 50, primary_key=True)
    username = models.CharField(max_length=50)
    song_pairings = models.ManyToManyField("SongPairing", related_name="users", blank = True)
    token = models.CharField(max_length=250, blank=True)

    def _song_pairings(self):
        return self.song_pairings

#id = auto gen number
#song_key = https://open.spotify.com/track/4CJ7iadNL15GuTr7fXMqxr
#song_values = [1, 2]
class SongPairing(models.Model):
    id = models.AutoField(primary_key=True)
    song_key = models.CharField(max_length=100)
    song_values = models.ManyToManyField("SongValues", related_name="song_pairings", blank = True)

    def _song_values(self):
        return self.song_values
    
#id = auto gen number
#song_uri = https://open.spotify.com/track/1BcuFfskHNf1WvqpyCs4wT
class SongValues(models.Model):
    id = models.AutoField(primary_key=True)
    song_uri = models.CharField(max_length=100)