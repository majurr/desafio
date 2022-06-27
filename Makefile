default: run

run:
	- docker-compose build --no-cache
	- docker-compose up -d

st:
	- docker ps -a
	- docker images -a

clc:
	- docker stop desafio-api-1 desafio-sql-1
	- docker rm desafio-api-1 desafio-sql-1

cli:
	- docker rmi desafio_api postgres:13-alpine

bash:
	- docker exec -it desafio-api-1 bash

log-api:
	- docker logs desafio-api-1 -f

log-sql:
	- docker logs desafio-sql-1 -f

reboot:
	- docker restart desafio-api-1

db:
	- docker exec -it desafio-sql-1 psql -h localhost -U desafio --dbname=desafio

black:
	- docker exec -it desafio-api-1 python -m black /app
