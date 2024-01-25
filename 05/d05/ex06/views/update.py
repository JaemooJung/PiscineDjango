from ..utils import *
from ..forms import *
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

TABLE_NAME = 'ex06_movies'

def update(request):
	conn = ex06_db_connect()
	
	if request.method == 'GET':
		select_query = f"""
			SELECT * FROM {TABLE_NAME};
		"""
		try:
			with conn.cursor() as curs:
				curs.execute(select_query)
				movies = curs.fetchall()
			context = {'form': UpdateForm(choices=((movie[0], movie[0]) for movie in movies))}
			return render(request, 'ex06/update.html', context)
		except:
			return HttpResponse("No data available")
		
	elif request.method == 'POST':
		select_query = f"""
		  SELECT title FROM {TABLE_NAME};
		"""

		update_query = f"""
			UPDATE {TABLE_NAME} SET opening_crawl = %s WHERE title = %s
		"""

		try:
			with conn.cursor() as curs:
				curs.execute(select_query)
				movies = curs.fetchall()
			choices = ((movie[0], movie[0]) for movie in movies)
		except Exception as e:
			print(e)
		data = UpdateForm(choices, request.POST)
		if data.is_valid():
			try:
				with conn.cursor() as curs:
					curs.execute(update_query, [
						data.cleaned_data['opening_crawl'], 
						data.cleaned_data['title']
						])
				conn.commit()
			except Exception as e:
				print(e)
		return redirect(request.path)