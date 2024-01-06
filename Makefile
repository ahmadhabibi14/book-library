setup-python:
	python -m venv .env
	source .venv/bin/activate
	python -m pip install Django
	pip install django-ratelimit
	pip install dotenv
	pip install inertia-django
	pip install django-vite
	pip install djangorestframework
	pip install django-cors-headers
	pip install -r requirements.txt

setup-js:
	pnpm install

update-dep:
	pip freeze > requirements.txt