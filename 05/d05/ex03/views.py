from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
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
    return render(request, 'ex03/display.html', {"movies": movies})
  except Exception as e:
    return HttpResponse(f"No data available: {e}")

