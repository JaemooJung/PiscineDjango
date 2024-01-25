from django.shortcuts import render
from ..models import Movies
from django.http import HttpResponse

def display(request):
  try:
    movies = Movies.objects.all()
    if len(movies) == 0:
      raise Movies.DoesNotExist
    return render(request, 'ex07/display.html', {"movies": movies})
  except Exception as e:
    return HttpResponse("No data available")