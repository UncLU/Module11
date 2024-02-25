import mysql.connector

# Подключение к базе данных
conn = mysql.connector.connect(
    host="ensembldb.ensembl.org",
    port="3306",
    user="anonymous",
    password="",
    database="homo_sapiens_core_101_38"
)

# Создание курсора
cursor = conn.cursor()

# Выполнение запроса
cursor.execute("SELECT * FROM gene LIMIT 10")

# Получение результатов запроса
results = cursor.fetchall()
for row in results:
    print(row)

# Закрытие курсора и соединения
cursor.close()
conn.close()
    execute_query(second_query)
