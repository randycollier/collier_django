build:
	docker-compose build

up:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

cli:
	docker-compose run --rm web bash

pdb:
	docker-compose stop web; docker-compose run --service-ports web

shell-web:
	docker exec -ti collier-web bash

shell-db:
	docker exec -ti collioer-postgres bash

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db 

collectstatic:
	docker exec collier-web /bin/sh -c "python manage.py collectstatic --noinput"  