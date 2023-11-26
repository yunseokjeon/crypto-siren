# [How to expose a local development server to the Internet](https://medium.com/botfuel/how-to-expose-a-local-development-server-to-the-internet-c31532d741cc)

# [유동 IP 변경 주기를 이해하고 공유기를 고정 IP처럼 바꿔주자](https://www.site.ne.kr/%EA%B3%B5%EC%9C%A0%EA%B8%B0-nas-%EC%9C%A0%EB%8F%99-ip-%EA%B3%A0%EC%A0%95-ip-%EB%8F%84%EB%A9%94%EC%9D%B8-ddns/)

# [How To Deploy Django Using Docker Compose On Windows In 9 Steps](https://medium.com/powered-by-django/deploy-django-using-docker-compose-windows-3068f2d981c4)

```
// Dockerfile

# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000
```

```
// requirements.txt 만들기
> pip freeze > requirements.txt
```

```
// MySQL in docker compose
// https://wecandev.tistory.com/107

version: '3'
services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    ports:
      - 3306:3306 # HOST:CONTAINER
    environment:
      MYSQL_ROOT_PASSWORD: admin
    command:
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
    volumes:
      - D:/mysql/data:/var/lib/mysql
```

```
// docker-compose.yml

version: '3.9'

services:
  db:
    image: postgres
    env_file:
      - .env
  web:
    build: .
    command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - .env
```

```
> docker compose build
> docker compose up -d
> docker compose logs web
```

