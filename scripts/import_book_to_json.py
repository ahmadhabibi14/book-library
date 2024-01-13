import requests
import json
import uuid

JSON_FINAL = []

PAGE_START = 1
TOTAL_BOOK = 20

API_URL = f"https://www.gramedia.com/api/algolia/search/product/?page={PAGE_START}&per_page={TOTAL_BOOK}&category=buku&based_on=new-arrival"
RESP = requests.get(API_URL)
if RESP.status_code == 200:
  JSON_DATA = RESP.json()
  FILE_PATH = 'Books.json'

  for item in JSON_DATA:
    book = {}
    id = uuid.uuid4()

    book['id'] = str(id)
    book['judul'] = item['name']
    book['rilis'] = item['publishDateTimestamp']
    book['thumbnail'] = item['thumbnail']
    book['slug'] = item['slug']
    if item['authors'][0]['title'] == None:
      book['penulis'] = 'unknown'
    else:
      book['penulis'] = item['authors'][0]['title']

    JSON_FINAL.append(book)

  with open(FILE_PATH, 'w') as json_file:
    json.dump(JSON_FINAL, json_file, indent=2)
  
  print(f"JSON data saved to {FILE_PATH}")
else:
  print(f"Failed to retrieve data. Status code: {RESP.status_code}")
