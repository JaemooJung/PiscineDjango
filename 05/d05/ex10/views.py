from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from .models import Movies
from django.http import HttpResponse

class Display(View):
  def get(self, request):
    form = SearchForm()
    return render(request, 'ex10/display.html', {'form': form})
  
  def post(self, request):
    try:
      form = SearchForm(request.POST)
      if form.is_valid():
        data = form.cleaned_data
        queryset = Movies.objects.filter(
                characters__gender=data['gender'],
                release_date__gte=data['min_release_date'],
                release_date__lte=data['max_release_date'],
                characters__homeworld__diameter__gt=data['min_planet_diameter']).order_by('release_date').values_list(
                    'title',
                    'characters__name',
                    'characters__gender',
                    'characters__homeworld__name',
                    'characters__homeworld__diameter')
        results = list(queryset)
        return render(request, 'ex10/display.html', {'form': form, 'results': results})
      else:
        raise Exception('Invalid form')
    except Exception as e:
      return HttpResponse(e)
    

