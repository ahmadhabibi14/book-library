setup-python:
	pip install --upgrade pip
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

setup-js:
	cd app
	pnpm install

update-dep:
	pip freeze > requirements.txt

install-dep:
	pip install -r requirements.txt

migration:
	docker exec web python3 manage.py makemigrations perpus
	python3 manage.py migrate

venv:
	python -m venv .venv
	source .venv/bin/activate

build:
	docker-compose -f docker-compose.prod.yml up -d --build