import json
import requests
import time

JSON_BOOK_DESC = []

JSON_FILE_PATH = 'Book_Desc.json'
JSON_BOOK_PATH = 'Books.json'

seen_names = set()
with open(JSON_BOOK_PATH, "r") as json_file:
  data = json.load(json_file)

  for item in data:
    book_desc = {}

    book_desc['id'] = item['id']
    book_desc['slug'] = item['slug']
    
    API_URL = f"https://www.gramedia.com/api/products/v3/meta_info/{item['slug']}"
    print(API_URL)
    RESP = requests.get(API_URL)
    if RESP.status_code == 200:
      JSON_DATA = RESP.json()
      if 'description' in JSON_DATA:
        book_desc['deskripsi'] = JSON_DATA['description']
      else:
        book_desc['deskripsi'] = 'Tidak ada deskripsi'
    else:
      book_desc['deskripsi'] = 'Tidak ada deskripsi'

    JSON_BOOK_DESC.append(book_desc)
    time.sleep(1)

with open(JSON_FILE_PATH, 'w') as json_file:
  json.dump(JSON_BOOK_DESC, json_file, indent=2)
  
  print(f"JSON data saved to {JSON_FILE_PATH}")