from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django import db
from .forms import *
from .utils import *
from .models import *

def populate(request):
  movie_data = starwars_movie_infos()
  result = []

  for movie in movie_data:
    try:
      movie_model = Movies(**movie)
      movie_model.save()
      result.append("OK")
    except Exception as e:
      result.append(e)
  
  return HttpResponse("<br/>".join(str(i) for i in result))

def display(request):
  try:
    movies = Movies.objects.all()
    if len(movies) == 0:
      raise Movies.DoesNotExist
    return render(request, 'ex05/display.html', {"movies": movies})
  except Exception as e:
    return HttpResponse("No data available")

def remove(request):
  if request.method == "GET":
    try:
      movies = Movies.objects.all()
      if len(movies) == 0:
        raise Movies.DoesNotExist
      context = {"form": RemoveForm((movie.title, movie.title) for movie in movies)}
      return render(request, 'ex05/remove.html', context)
    except Exception as e:
      return HttpResponse("No data available")
    
  elif request.method == "POST":
    try:
      movies = Movies.objects.all()
      if len(movies) == 0:
          raise Movies.DoesNotExist
    except Movies.DoesNotExist as e:
        return HttpResponse("No data available")
    data = RemoveForm(((movie.title, movie.title) for movie in movies), request.POST)
    if data.is_valid():
        try:
            Movies.objects.get(title=data.cleaned_data['title']).delete()
        except db.Error as e:
            print(e)
    return redirect(request.path)