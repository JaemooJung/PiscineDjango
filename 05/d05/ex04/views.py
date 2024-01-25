from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .utils import *
from .forms import *
import psycopg2

TABLE_NAME = 'ex04_movies'

# Init
def init(request):
  try:
    conn = ex04_db_connect()
    query = f"""
      CREATE TABLE {TABLE_NAME}(
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb INT PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
        );
      """
    with conn.cursor() as curs:
      curs.execute(query)
    conn.commit()
    return HttpResponse("OK")
  except Exception as e:
    return HttpResponse(str(e))

# Populate
def populate(request):
  try:
    conn = ex04_db_connect()
    query = f"""
      INSERT INTO {TABLE_NAME} (
        episode_nb,
        title,
        director,
        producer,
        release_date
        )
      VALUES (
        %(episode_nb)s,
        %(title)s,
        %(director)s,
        %(producer)s,
        %(release_date)s
        );
    """
    result = []

    with conn.cursor() as curs:
      for movie in starwars_movie_infos():
        try:
          curs.execute(query, movie)
          conn.commit()
          result.append("OK")
        except psycopg2.DatabaseError as e:
          conn.rollback()
          result.append(e)
    return HttpResponse("<br/>".join(str(i) for i in result))
  
  except Exception as e:
    return HttpResponse(str(e))

# Display
def display(request):
  try:
      conn = ex04_db_connect()
      query = f"""
          SELECT * FROM {TABLE_NAME};
          """
      
      with conn.cursor() as curs:
          curs.execute(query)
          movies = curs.fetchall()
      return render(request, 'ex04/display.html', {"movies": movies})
  except:
      return HttpResponse("No data available")

# Remove
def remove(request):
  conn = ex04_db_connect()

  if request.method == 'GET':
    query = f"""
      SELECT title FROM {TABLE_NAME};
    """
    try:
      with conn.cursor() as curs:
        curs.execute(query)
        movies = curs.fetchall()
      context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
      return render(request, 'ex04/remove.html', context)
    except:
      return HttpResponse("No data available")
    
  elif request.method == 'POST':
    select_query = f"""
      SELECT title FROM {TABLE_NAME};
    """
    delete_query = f"""
      DELETE FROM {TABLE_NAME} WHERE title = %s
    """

    try:
      with conn.cursor() as curs:
          curs.execute(select_query)
          movies = curs.fetchall()
      choices = ((movie[0], movie[0]) for movie in movies)
    except Exception as e:
        print(e)
    
    data = RemoveForm(choices, request.POST)
    if data.is_valid():
        try:
            with conn.cursor() as curs:
                curs.execute(delete_query, [data.cleaned_data['title']])
            conn.commit()
        except Exception as e:
            print(e)
    return redirect(request.path)


