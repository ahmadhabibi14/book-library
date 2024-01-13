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

JSON_BOOK_PATH = 'Books.json'
JSON_AUTHOR_PATH = 'Authors.json'
JSON_BOOKDESC_PATH = 'Book_Desc.json'

SQL_TABLE = 'perpus_buku'
SQL_COLUMNS = [
  'id', 'judul', 'rilis', 'thumbnail', 'slug', 'deskripsi', 'penulis_id'
]

try:
  connection = mysql.connector.connect(**db_config)
  cursor = connection.cursor()

  author_json = json.load(open(JSON_AUTHOR_PATH))
  book_json = json.load(open(JSON_BOOK_PATH))
  book_desc_json = json.load(open(JSON_BOOKDESC_PATH))

  for item in book_json:
    id = item['id']
    judul = item['judul']

    rilis = datetime.datetime.utcfromtimestamp(item['rilis'])
    thumbnail = item['thumbnail']
    slug = item['slug']
    for book_desc in book_desc_json:
      if book_desc['slug'] == item['slug']:
        deskripsi = book_desc['deskripsi']

    penulis = item['penulis']

    for author in author_json:
      if author['nama'] == penulis:
        penulis = author['id']
        query = 'INSERT INTO ' + SQL_TABLE + ' ('+ ', '.join(SQL_COLUMNS) +') VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (id, judul, rilis, thumbnail, slug, deskripsi, penulis))
        connection.commit()


  print('Berhasil memasukkan data '+SQL_TABLE+' ke database')
except mysql.connector.Error as err:
  print(f"Error: {err}")

finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
