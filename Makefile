setup-python:
	python -m venv .env
	source .venv/bin/activate
	pip install -r requirements.txt

setup-js:
	pnpm install

update-dep:
	pip freeze > requirements.txt