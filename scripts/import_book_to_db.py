import json
import os
import uuid
import datetime
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_config = {
  'host': os.environ.get('MARIADB_HOST'),
  'user': os.environ.get('MARIADB_USER'),
  'password': os.environ.get('MARIADB_PASSWORD'),
  'database': os.environ.get('MARIADB_DATABASE'),
}

JSON_FILE_PATH = 'Books.json'
JSON_AUTHOR_PATH = 'Authors.json'

SQL_TABLE = 'perpus_buku'
SQL_COLUMNS = [
  'id', 'judul', 'rilis', 'thumbnail', 'penulis'
]

try:
  connection = mysql.connector.connect(**db_config)
  cursor = connection.cursor()

  author_json = json.load(open(JSON_AUTHOR_PATH))
  book_json = json.load(open(JSON_FILE_PATH))

  for item in book_json:
    id = item['id']
    judul = item['judul']

    rilis = datetime.datetime.utcfromtimestamp(item['rilis'])
    thumbnail = item['thumbnail']
    penulis = item['penulis']

    for author in author_json:
      if author['nama'] == penulis:
        penulis = author['id']
        query = ''' INSERT INTO ''' + SQL_TABLE + ''' (id, judul, rilis, thumbnail, penulis_id) VALUES (%s, %s, %s, %s, %s) '''
        cursor.execute(query, (id, judul, rilis, thumbnail, penulis))
        connection.commit()


  print('Berhasil memasukkan data '+SQL_TABLE+' ke database')
except mysql.connector.Error as err:
  print(f"Error: {err}")

finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
