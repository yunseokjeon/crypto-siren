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

[Docker 컨테이너에 데이터 저장 (볼륨/바인드 마운트)](https://www.daleseo.com/docker-volumes-bind-mounts/)

# MySQL 새로운 사용자 추가하기

```SQL
show databases;
use siren;
create user 'yun'@'%' identified by '<PASSWORD>';
GRANT ALL privileges ON siren.* TO 'yun'@'%';
flush privileges;
```

```
> docker exec -it mysql-container bash
> mysql --verbose --help | grep my.cnf
```

# --noreload

```
> python manage.py runserver --noreload 0.0.0.0:8000
```

[Execute code when Django starts ONCE only?](https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only)

# Docker image 빌드하기

```
> docker build -t watcher .
> docker run --name watcher-container -d -p 8000:8000 watcher
> docker start watcher-container
> docker logs watcher-container
```

# Django migration

```
> python manage.py makemigrations tower
> python manage.py migrate tower

> python manage.py shell
> from tower.models import *
```

# Error Code: 1044: Access denied for user ' ' '@' '%' to database

```
GRANT ALL PRIVILEGES ON *.* TO 'yun'@'%' WITH GRANT OPTION;
```

# How to know database size

```SQL
SELECT table_schema AS "Database", 
ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS "Size (MB)" 
FROM information_schema.TABLES 
GROUP BY table_schema;
```

# UTC 기준 1분 전 부터 데이터 조회

```SQL
# 현재 시간(KST)을 UTC로 변환하기
select convert_tz(now(), '+00:00', '-09:00');

select date_sub(convert_tz(now(), '+00:00', '-09:00'), interval 1 minute);

select *
from tower_cryptoticker
where register_date
          between date_sub(convert_tz(now(), '+00:00', '-09:00'), interval 1 minute)
          and convert_tz(now(), '+00:00', '-09:00')
order by register_date desc;

select *
from tower_cryptotrade
where register_date
          between date_sub(convert_tz(now(), '+00:00', '-09:00'), interval 1 minute)
          and convert_tz(now(), '+00:00', '-09:00')
order by register_date desc;

select *
from tower_cryptoorderbookmain
where register_date
          between date_sub(convert_tz(now(), '+00:00', '-09:00'), interval 1 minute)
          and convert_tz(now(), '+00:00', '-09:00')
order by register_date desc;

select *
from tower_cryptoorderbooksub
where register_date
          between date_sub(convert_tz(NOW(), '+00:00', '-09:00'), interval 1 minute)
          and convert_tz(NOW(), '+00:00', '-09:00')
order by register_date desc;

```

