from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .utils import *

TABLE_NAME = 'ex02_movies'

def init(request):
  try:
    conn = ex02_db_connect()

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
    return HttpResponse(e)

def populate(request):
  try:
    conn = ex02_db_connect()
  
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
    return HttpResponse(e)

def display(request):
    try:
        conn = ex02_db_connect()


        query = f"""
            SELECT * FROM {TABLE_NAME};
            """
        with conn.cursor() as curs:
            curs.execute(query)
            movies = curs.fetchall()
        return render(request, 'ex02/display.html', {"movies": movies})
    except Exception as e:
        return HttpResponse(e)

