This project aims to collect data from cryptocurrency exchanges and is still ongoing.

# Setting config files

1) crypto-siren/watcher/config/config.ini

```
[Upbit]
upbit_key=<YourKey>
upbit_secret=<YourSecret>

[MySQL]
name=<YourName>
user=<YourUser>
password=<YourPassword>
host=<YourIP>
port=<YourPort>

[Docker]
isDocker=docker_local  
```

2) crypto-siren/watcher/.env

```
MYSQL_ROOT_PASSWORD=<YourPassword>
```

# Setting MySQL

```
> docker -v
> docker pull mysql
> docker images
> docker volume create mysql-volume
> docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -v mysql-volume:/var/lib/mysql -d -p  3306:3306 mysql:latest
```

# Adding new user in MySQL

```
show databases;
create database siren;
use siren;
create user 'yun'@'%' identified by '<PASSWORD>';
GRANT ALL privileges ON siren.* TO 'yun'@'%';
flush privileges;
```

# Building a docker image and run a container

Before running a container, migrate schema using `python manage.py migrate tower`.

```
> cd watcher
> docker build -t watcher .
> docker run --name watcher-container -d -p 8000:8000 watcher
```

