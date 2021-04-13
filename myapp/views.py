from django.shortcuts import render, redirect

from myapp.form import CastForm, MovieForm
from myapp.models import Movie, Cast


def welcomepage(request):
    return render(request, 'myapp/welcomepage.html', {'a': 'My Welcome Page', 'b': 'your wp'})

def movieadd(request):
    if request.method == "POST":
        movie = MovieForm(request.POST)
        movie.save()
        return redirect('/myapp/movie/show')
    else:
        form = MovieForm
        return render(request, 'myapp/movieadd.html', {'form': form})

def castadd(request):
    if request.method == 'POST':
        form = CastForm(request.POST)
        form.save()
        return redirect('/myapp/cast/show')
    else:
        form = CastForm
        return render(request, 'myapp/castadd.html', {'form': form})

def castshow(request):
    list = Cast.objects.all()
    return render(request, 'myapp/castshow.html', {'list': list})

def movieshow(request):
    list = Movie.objects.all()
    return render(request, 'myapp/movieshow.html', {'list': list})

# Create your views here.
