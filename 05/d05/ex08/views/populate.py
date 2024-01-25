from django.views import View
from django.http import HttpResponse
from ..utils import *
import csv

class Populate(View):
  conn = ex08_db_connect()

  insert_planet_query = """
  INSERT INTO ex08_planets (
    name,
    climate,
    diameter,
    orbital_period,
    population,
    rotation_period,
    surface_water,
    terrain
  ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )
  """

  insert_people_query = """
  INSERT INTO ex08_people (
    name,
    birth_year,
    gender,
    eye_color,
    hair_color,
    height,
    mass,
    homeworld
  ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )
  """
  
  def get(self, request):
    result = []
    planet_list = []
    people_list = []
    try:
      planet_list = csv_to_list('static/planets.csv')
      people_list = csv_to_list('static/people.csv')
    except Exception as e:
      return HttpResponse(e)
    
    for planet in planet_list:
      try:
        with self.conn.cursor() as curs:
          curs.execute(self.insert_planet_query, planet)
          result.append("OK")
          self.conn.commit()
      except Exception as e:
        self.conn.rollback()
        result.append(e)
    
    for people in people_list:
      try:
        with self.conn.cursor() as curs:
          curs.execute(self.insert_people_query, people)
          result.append("OK")
          self.conn.commit()
      except Exception as e:
        self.conn.rollback()
        result.append(e)

    return HttpResponse("<br/>".join(str(i) for i in result))




