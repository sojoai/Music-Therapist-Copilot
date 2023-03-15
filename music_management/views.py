from django.shortcuts import render
from .models import Song, Playlist
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PlaylistSerializer, SongSerializer


# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]


def display_songs(request):
    items = Song.objects.all()
    context = {
        'items': items,
    }
    print(items)
    return render(request, "music/songs.html", context)
