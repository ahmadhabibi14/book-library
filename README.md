## Perpus

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

##### Start development
```shell
python manage.py runserver
```