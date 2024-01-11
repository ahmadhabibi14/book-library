import json
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_config = {
  'host': os.environ.get('MARIADB_HOST'),
  'user': os.environ.get('MARIADB_USER'),
  'password': os.environ.get('MARIADB_PASSWORD'),
  'database': os.environ.get('MARIADB_DATABASE'),
}

JSON_FILE_PATH = 'Authors.json'

SQL_TABLE = 'perpus_penulis'
SQL_COLUMNS = [
  'id', 'nama'
]

try:
  connection = mysql.connector.connect(**db_config)
  cursor = connection.cursor()

  with open(JSON_FILE_PATH, "r") as json_file:
    data = json.load(json_file)

    for item in data:
      id = item['id']
      nama = item['nama']
      query = ''' INSERT INTO ''' + SQL_TABLE + ''' (id, nama) VALUES (%s, %s)'''

      cursor.execute(query, (id, nama))
      connection.commit()

  print('Berhasil memasukkan data '+SQL_TABLE+' ke database')
except mysql.connector.Error as err:
  print(f"Error: {err}")

finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
