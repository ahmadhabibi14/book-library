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

##### Import books
```shell
cd scripts
./xImportBook.sh
```

##### Start development
```shell
python manage.py runserver
```