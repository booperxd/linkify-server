from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.SongPairing)
# Register your models here.
