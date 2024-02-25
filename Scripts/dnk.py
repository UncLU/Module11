import psycopg2

def execute_query(sql_query):
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="Rfam",
        user="rfamro",
        password="none",
        host="mysql-rfam-public.ebi.ac.uk",
        port="4497"
    )

# Создание курсора для выполнения запросов
cur = conn.cursor()

# SQL-запрос
sql_query = "SELECT * FROM таблица WHERE условие;"

# Выполнение запроса
cur.execute(sql_query)

# Получение результатов
results = cur.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие курсора и соединения
cur.close()
conn.close()
