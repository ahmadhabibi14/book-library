import json
import uuid

JSON_BOOK = []
JSON_FILE_PATH = 'Authors.json'
JSON_BOOK_PATH = 'Books.json'

seen_names = set()
with open(JSON_BOOK_PATH, "r") as json_file:
  data = json.load(json_file)

  for item in data:
    author = {}

    if item['penulis'] in seen_names:
      continue
    else:
      seen_names.add(item['penulis'])
      id = uuid.uuid4()
      author['id'] = str(id)
      author['nama'] = item['penulis']
      
      JSON_BOOK.append(author)

with open(JSON_FILE_PATH, 'w') as json_file:
  json.dump(JSON_BOOK, json_file, indent=2)
  
  print(f"JSON data saved to {JSON_FILE_PATH}")