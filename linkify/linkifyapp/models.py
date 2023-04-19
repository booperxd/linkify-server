from django.db import models
#This might given an error. Refer to this https://stackoverflow.com/questions/70656495/importerror-cannot-import-name-ugettext-lazy
import jsonfield

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    song_pairings = models.ManyToManyField("SongPairing", related_name="song_pairings", blank = True)

    def _song_pairings(self):
        return self.song_pairings

class SongPairing(models.Model):
    id = models.AutoField(primary_key=True)
    song_key = models.CharField(max_length=100)
    song_values = jsonfield.JSONField()

    def _song_values(self):
        return self.song_values