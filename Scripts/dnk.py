import psycopg2

def execute_query(sql_query):
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="Rfam",
        user="пользователь",
        password="none",
        host="хост",
        port="4497"
    )

    # Создание курсора для выполнения запросов
    cur = conn.cursor()

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

if __name__ == "__main__":
    # Выполнение первого запроса
    print("First Query:")
    first_query = "SELECT * FROM fr.fram_acc LIMIT 1;"
    execute_query(first_query)

    # Выполнение второго запроса
    print("Second Query:")
    second_query = """
    SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
    FROM full_region fr, rfamseq rf, taxonomy tx
    WHERE rf.ncbi_id = tx.ncbi_id
    AND fr.rfamseq_acc = rf.rfamseq_acc
    AND tx.ncbi_id = 10116
    AND is_significant = 1;
    """
    execute_query(second_query)
