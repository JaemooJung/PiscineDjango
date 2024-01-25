from ..utils import ex08_db_connect
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class Display(View):
    template = 'ex08/display.html'
    table_planets = "ex08_planets"
    table_people = "ex08_people"
    conn = ex08_db_connect()

    SELECT_TABEL = f"""
      SELECT
        {table_people}.name,
        {table_people}.homeworld,
        {table_planets}.climate
      FROM
        {table_planets}
        RIGHT JOIN {table_people}
        ON
          {table_people}.homeworld = {table_planets}.name
          where
            {table_planets}.climate
            LIKE '%windy%'
        ORDER BY {table_planets}.name;
    """

    def get(self, request):
        try:
            with self.conn.cursor() as curs:
                curs.execute(self.SELECT_TABEL)
                datas = curs.fetchall()
            return render(request, self.template, {'datas': datas})
        except Exception as e:
            return HttpResponse("No data available")