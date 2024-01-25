from ..utils import *
from django.http import HttpResponse
from django.views import View

class Init(View):
    conn = ex08_db_connect()

    def get(self, request):
        try:
            CREATE_TABEL = f"""
            CREATE TABLE ex08_planets(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INT,
                orbital_period INT,
                population BIGINT,
                rotation_period INT,
                surface_water REAL,
                terrain VARCHAR(128)
                );

            CREATE TABLE ex08_people(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
                );
            """

            with self.conn.cursor() as curs:
                curs.execute(CREATE_TABEL)
            self.conn.commit()
            return HttpResponse("OK")   
        except Exception as e:
            return HttpResponse(e)
