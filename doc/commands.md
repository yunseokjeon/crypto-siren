# MySQL

```
> docker -v
> docker pull mysql
> docker images

> docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:latest

> docker ps -a

# MySQL Docker 컨테이너 중지
> docker stop mysql-container

# MySQL Docker 컨테이너 시작
> docker start mysql-container

# MySQL Docker 컨테이너 재시작
> docker restart mysql-container

# MySQL Docker 컨테이너 접속
> docker exec -it mysql-container bash

# 데이터베이스 만들기
> mysql -u root -p
mysql> CREATE DATABASE siren;
```

[Docker를 사용하여 MySQL 설치하고 접속하기](https://poiemaweb.com/docker-mysql)

# Docker MySQL and -v

```
> docker volume create testdb-volume
> docker volume ls
> docker run --rm -d --name testdb -e MYSQL_ROOT_PASSWORD=mirero -v testdb-volume:/var/lib/mysql mysql
```

[Docker Volume 개념 및 MySql을 Docker상에서 운용하는 방법](https://joonhwan.github.io/2018-11-14-fix-mysql-volume-share-issue/)

# --noreload

```
> python manage.py runserver --noreload 0.0.0.0:8000
```

[Execute code when Django starts ONCE only?](https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only)

