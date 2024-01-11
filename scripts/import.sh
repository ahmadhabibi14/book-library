#!/bin/bash

set -x
set -e

echo "Importing..."

python import_book_to_json.py
echo "Imported book to JSON!"

python import_author_to_json.py
echo "Imported author to JSON!"

python import_author_to_db.py
echo "Imported Author to Database!"

python import_book_to_db.py
echo "Imported Book to Database!"

echo "Done!"