```
export DJANGO_PORT=8080
export DJANGO_DATA=./pg_data
export COMPOSE_PROJECT_NAME=master
docker-compose -f docker-compose.yml -f docker-compose-production.yml build
docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d
```