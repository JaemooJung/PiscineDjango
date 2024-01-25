from django.conf import settings
import psycopg2
import csv

def ex08_db_connect():
  return psycopg2.connect(
    dbname=settings.DATABASES['default']['NAME'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    host=settings.DATABASES['default']['HOST'],
    port=settings.DATABASES['default']['PORT'],
  )

def csv_to_list(path):
  with open(path) as file:
    reader = csv.reader(file, delimiter='\t')
    return [[None if value == 'NULL' else value for value in row] for row in reader]
  
