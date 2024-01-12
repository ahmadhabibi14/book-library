#!/bin/bash

set -x
set -e

echo "Importing..."

python ./scripts/import_book_to_json.py
echo "Imported book to JSON!"

python ./scripts/import_author_to_json.py
echo "Imported author to JSON!"

python ./scripts/import_author_to_db.py
echo "Imported Author to Database!"

python ./scripts/import_book_to_db.py
echo "Imported Book to Database!"

echo "Done!"