#!/bin/bash

# Остановка и удаление всех контейнеров
docker-compose down

# Остановка всех контейнеров, если они существуют
if [ "$(docker ps -q)" ]; then
    docker stop $(docker ps -q)
fi

# Удаление всех контейнеров, если они существуют
if [ "$(docker ps -a -q)" ]; then
    docker rm $(docker ps -a -q)
fi

# Удаление всех образов, если они существуют
if [ "$(docker images -q)" ]; then
    docker rmi $(docker images -q)
fi

# Удаление всех томов, если они существуют
if [ "$(docker volume ls -q)" ]; then
    docker volume rm $(docker volume ls -q)
fi

# Удаление всех сетей, если они существуют
if [ "$(docker network ls -q | grep -v 'bridge\|host\|none')" ]; then
    docker network rm $(docker network ls -q | grep -v 'bridge\|host\|none')
fi

# Удаление кэша сборки
docker builder prune -f

echo "Все контейнеры, образы, тома, сети и кэш Docker удалены."
