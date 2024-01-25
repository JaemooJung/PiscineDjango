from django.http import HttpResponse
from django.shortcuts import render,redirect
from ..models import Movies
from ..forms import UpdateForm

def update(request):
    if request.method == "GET":
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
            context = {"form": UpdateForm((movie.title, movie.title) for movie in movies)}
            return render(request, 'ex07/update.html', context)
        except Exception as e:
            return HttpResponse("No data available")
    
    elif request.method == "POST":
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
            form = UpdateForm(((movie.title, movie.title) for movie in movies), request.POST)
            if form.is_valid():
                try:
                    movie = Movies.objects.get(title=form.cleaned_data["title"])
                    movie.opening_crawl = form.cleaned_data["opening_crawl"]
                    movie.save()
                except Exception as e:
                    print(e)
            return redirect(request.path)
        except Exception as e:
            return redirect(request.path)