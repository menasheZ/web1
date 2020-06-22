from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Album, Song

# Create your views here.

def index(request):
    all_album = Album.objects.all()
    context = {'all_albums': all_album}
    return render(request,'music/index.html', context)

def index1(request):
    return HttpResponse("music1")

def detail(request, album_id):
   album = get_object_or_404(Album, pk=album_id)
   return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album, 'error_massage': "no Song"})
    else:
        selected_song.is_favorite = not selected_song.is_favorite
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album })


