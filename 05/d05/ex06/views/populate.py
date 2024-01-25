from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from ..utils import *
import psycopg2

TABLE_NAME = 'ex06_movies'

# Populate
def populate(request):
  try:
    conn = ex06_db_connect()
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