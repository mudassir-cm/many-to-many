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
def castedit(request, id):
    cast = Cast.objects.get(id=id)
    return render(request, 'myapp/castedit.html', {'cast': cast})
def castupdate(request, id):
    cast = Cast.objects.get(id=id)
    cast.name = request.POST['name']
    cast.age = request.POST['age']
   # castform = CastForm(request.POST, instance=cast)
    cast.save()
    return redirect('/myapp/cast/show')

def castdelete(request, id):
    cast = Cast.objects.get(id=id)
    cast.delete()
    return redirect('/myapp/cast/show')

def movieshow(request):
    list = Movie.objects.all()
    return render(request, 'myapp/movieshow.html', {'list': list})

def moviedelete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/myapp/movie/show')

def movieedit(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'myapp/movieedit.html', {'movie': movie})

def movieupdate(request, id):
    movie =  Movie.objects.get(id=id)
    movie.name = request.POST['name']
    movie.dor = request.POST['dor']
   # movieform = MovieForm(request.POST, instance=movie)
    movie.save()
    return redirect('/myapp/movie/show')
# Create your views here.