## Запуск селери воркер на виндовс
celery -A config worker -l info -P solo     

## Запуск селери бит на виндовс 
 celery -A config beat -l INFO

## Создание и запуск контейнеров
docker-compose up -d --build

