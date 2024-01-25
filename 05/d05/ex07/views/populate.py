from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django import db
from ..forms import *
from ..utils import *
from ..models import *

def populate(request):
  result = []

  for movie in starwars_movie_infos():
    try:
      movie_model = Movies(**movie)
      movie_model.save()
      result.append("OK")
    except Exception as e:
      result.append(e)
  
  return HttpResponse("<br/>".join(str(i) for i in result))