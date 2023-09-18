from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracks
from .models import Titles
from .models import Artists
from .models import Albums
from .forms import TracksForm
from django.views.generic import DetailView

# Create your views here.

class TracksDetailView(DetailView):
    model = Tracks
    template_name = 'main/track.html'
    context_object_name = 'song'

    def get_context_data(self, **kwargs):
        context = super(TracksDetailView, self).get_context_data(**kwargs)
        context['album'] = Albums.objects.all()
        context['title'] = Titles.objects.all()
        return context

def index(request):
    tracks = Tracks.objects.all()
    return render(request, 'main/index.html', {'tracks': tracks})

def post(request):
    form = TracksForm()
    data = {
        'form': form,
    }
    return render(request, 'main/post.html', data)

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        artist = request.POST['artist']
        album = request.POST['album']
        track_number = request.POST['track_number']
        tempo = request.POST['tempo']
        duration = request.POST['duration']
        isrc_code = request.POST['isrc_code']
        explict = request.POST['explict']

        real_title = Titles.objects.get(id=title)
        real_artist = Artists.objects.get(id=artist)
        real_album = Albums.objects.get(id=album)
        if explict == "on":
            real_explict = 1
        else:
            real_explict = 0

        newtrack = Tracks(title=real_title, artist=real_artist, album=real_album, track_number=track_number, tempo=tempo, duration=duration, isrc_code=isrc_code, explict=real_explict)
        newtrack.save()
        success = str(real_artist) + ' - ' + str(real_title) + ' добавлена в базу данных'
        return HttpResponse(success)