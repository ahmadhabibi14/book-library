setup-python:
	pip install --upgrade pip
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

setup-js:
	npm install

update-dep:
	pip freeze > requirements.txt

install-dep:
	pip install -r requirements.txt

migration:
	python manage.py makemigrations perpus
	python manage.py migrate

venv:
	python -m venv .venv
	source .venv/bin/activate

build:
	pnpm build
	python manage.py collectstatic

setup-linux:
	sudo apt update \
	sudo apt install \
	python3-dev default-libmysqlclient-dev python3-pip python3-venv \
	nodejs npm