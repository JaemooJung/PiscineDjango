from django.conf import settings
import psycopg2

def ex04_db_connect():
  return psycopg2.connect(
    dbname=settings.DATABASES['default']['NAME'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
    )

def starwars_movie_infos():
  return [
    {
      'episode_nb': 1,
      'title': 'The Phantom Menace',
      'director': 'George Lucas',
      'producer': 'Rick McCallum',
      'release_date': '1999-05-19',
    },
    {
      'episode_nb': 2,
      'title': 'Attack of the Clones',
      'director': 'George Lucas',
      'producer': 'Rick McCallum',
      'release_date': '2002-05-16',
    },
    {
      'episode_nb': 3,
      'title': 'Revenge of the Sith',
      'director': 'George Lucas',
      'producer': 'Rick McCallum',
      'release_date': '2005-05-19',
    },
    {
      'episode_nb': 4,
      'title': 'A New Hope',
      'director': 'George Lucas',
      'producer': 'Gary Kurtz, Rick McCallum',
      'release_date': '1977-05-25',
    },
    {
      'episode_nb': 5,
      'title': 'The Empire Strikes Back',
      'director': 'Irvin Kershner',
      'producer': 'Gary Kutz, Rick McCallum',
      'release_date': '1980-05-17',
    },
    {
      'episode_nb': 6,
      'title': 'Return of the Jedi',
      'director': 'Richard Marquand',
      'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
      'release_date': '1983-05-25',
    },
    {
      'episode_nb': 7,
      'title': 'The Force Awakens',
      'director': 'J. J. Abrams',
      'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
      'release_date': '2015-12-11',
    },
  ]