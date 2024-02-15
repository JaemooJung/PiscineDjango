from django.shortcuts import render
from ..utils import *
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

TABLE_NAME = 'ex06_movies'

def display(request):
  try:
      conn = ex06_db_connect()
      query = f"""
          SELECT * FROM {TABLE_NAME};
          """
      
      with conn.cursor() as curs:
        curs.execute(query)
        movies = curs.fetchall()
        if len(movies) == 0:
            raise psycopg2.Error
      return render(request, 'ex06/display.html', {"movies": movies})
  except:
      return HttpResponse("No data available")