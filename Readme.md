
Installation
---
Build and run via `docker-compose up`

run migrations via `docker-compose exec web python b_test_task/manage.py migrate --noinput`

run tests via `docker-compose exec web python b_test_task/manage.py test event`