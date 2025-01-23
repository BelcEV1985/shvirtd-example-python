#!/bin/bash

# Определяем путь к текущей директории
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Загружаем переменные из файла .env
source "$SCRIPT_DIR/.env"

# Директория для резервных копий
BACKUP_DIR="/opt/backup"

# Создаем директорию для резервных копий, если она не существует
mkdir -p $BACKUP_DIR

# Генерируем имя файла резервной копии
TIMESTAMP=$(date +"%F-%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql"

# Выводим информацию для отладки
echo "Starting backup..."
echo "Backup directory: $BACKUP_DIR"
echo "Backup file: $BACKUP_FILE"

# Выполняем резервное копирование
docker run --network backend -v $BACKUP_DIR:/backup schnitzler/mysqldump -h $DB_HOST -P $DB_PORT -u $DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_FILE 2>&1
