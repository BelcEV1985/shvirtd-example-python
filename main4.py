import os
import mysql.connector
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

db_host = os.environ.get('DB_HOST', '127.0.0.1')
db_user = os.environ.get('DB_USER', 'app')
db_password = os.environ.get('DB_PASSWORD', 'very_strong')
db_database = os.environ.get('DB_NAME', 'example')
table_name = os.environ.get('TABLE_NAME', 'requests')

# Подключение к базе данных MySQL
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    autocommit=True
)
cursor = db.cursor()

# SQL-запрос для создания таблицы в БД
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
id INT AUTO_INCREMENT PRIMARY KEY,
request_date DATETIME,
request_ip VARCHAR(255)
)
"""
cursor.execute(create_table_query)

@app.route('/')
def index():
    # Получение IP-адреса пользователя
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    # Запись в базу данных
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    query = f"INSERT INTO {table_name} (request_date, request_ip) VALUES (%s, %s)"
    values = (current_time, ip_address)
    cursor.execute(query, values)
    db.commit()
    return f'TIME: {current_time}, IP: {ip_address}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

