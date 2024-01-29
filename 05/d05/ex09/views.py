from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import People

class Display(View):

  def get(self, request):
    try:
      people = People.objects.filter(homeworld__climate__contains='windy').order_by('name')
      if len(people) == 0:
        raise People.DoesNotExist
      return render(request, 'ex09/display.html', {'people': people })
    except Exception as e:
      print(e)
      return HttpResponse("No data available, please use the following command line before use: \
                           python3 manage.py loaddata static/ex09_initial_data.json")
