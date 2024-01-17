## ePerpus

![My Dotties](/web/assets/img/Covers.png)

#### Migration
```shell
python manage.py makemigrations perpus
python manage.py migrate perpus
```

##### Connect Docker
```shell
docker-compose up -d

docker exec -it perpus-db mariadb -u perpus -p
# password: perpus123
```

##### Install Dependencies
```shell
pip install --upgrade pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# OR
make setup-python
# OR
make install-dep
```

##### Update Dependencies
```shell
# If there is a new library installed
make update-dep
```

#### Install NodeJS dependencies
```shell
npm install
# OR
pnpm install
```

##### Import books
```shell
cd scripts
./xImportBook.sh
```

##### Start development
```shell
./start.sh

# And run Vite + Svelte
pnpm dev
```