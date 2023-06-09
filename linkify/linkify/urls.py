"""
URL configuration for linkify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from linkifyapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name = "index"),
    path("current", views.get_current_song, name = "current_song"),
    path("check-songs", views.compare_songs, name = "check client song"),
    path("users", views.UserView.as_view(), name = "user view"),
    path("users/<str:pk>", views.SpecificUserView.as_view(), name = "specific user view"),
    path("song-pairings", views.SongPairingView.as_view(), name = "song pairing view"),
    path("song-pairings/<int:pk>", views.SpecificSongPairingView.as_view(), name = "specific song pairing view"),
    #path("song-values", views.SongValuesView.as_view(), name = "song value view"),
    #path("song-values/<int:pk>", views.SpecificSongValuesView.as_view(), name = "specific song value view"),
    
]
