#!/bin/bash

# URL вашего fork-репозитория
REPO_URL="https://github.com/BelcEV1985/shvirtd-example-python.git"
REPO_DIR="/opt/shvirtd-example-python"

# Клонируем репозиторий, если он не существует
if [ ! -d "$REPO_DIR" ]; then
  git clone $REPO_URL $REPO_DIR
fi

# Переходим в каталог репозитория
cd $REPO_DIR

# Запускаем Docker Compose
docker compose up --build
