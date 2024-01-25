from django.http import HttpResponse, HttpRequest
from ..utils import ex06_db_connect

TABLE_NAME = 'ex06_movies'

# Init
def init(request):
  try:
    conn = ex06_db_connect()
    query = f"""
      CREATE TABLE {TABLE_NAME}(
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb INT PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT NOW(),
        updated TIMESTAMP NOT NULL DEFAULT NOW()
        );
      
      CREATE OR REPLACE FUNCTION update_changetimestamp_column()
      RETURNS TRIGGER AS $$
      BEGIN
        NEW.updated = now();
        NEW.created = OLD.created;
        RETURN NEW;
      END;
      $$ language 'plpgsql';

      CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
      ON {TABLE_NAME} FOR EACH ROW EXECUTE PROCEDURE
      update_changetimestamp_column();
      """
    with conn.cursor() as curs:
      curs.execute(query)
    conn.commit()
    return HttpResponse("OK")
  except Exception as e:
    return HttpResponse(str(e))
  
