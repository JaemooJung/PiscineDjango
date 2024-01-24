from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import TextInput
from django.conf import settings
import logging

# Create your views here.

def index(request):
  logger = logging.getLogger('history')

  if request.method == 'POST':
    form = TextInput(request.POST)
    if form.is_valid():
      logger.info(form.cleaned_data['text'])
      return redirect('/ex02')

  try:
    with open(settings.EX_02_LOG_FILE, 'r') as f:
      histories = [line for line in f.readlines()]
  except:
    histories = []

  context = {
    'form': TextInput(),
    'histories': histories,
  }
  return render(request, 'ex02/index.html', context)
  

