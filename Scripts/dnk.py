import mysql.connector

def execute_query(sql_query):
    try:
        # Подключение к базе данных
        conn = mysql.connector.connect(
                host="ensembldb.ensembl.org",
                port="3306",
                user="anonymous",
                password="",
                database="homo_sapiens_core_101_38"
        )
        
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("Error executing query:", error)

if __name__ == "__main__":
    first_query = "SELECT * FROM regulatory_feature LIMIT 10;"
    execute_query(first_query)

    second_query = "SELECT * FROM dna LIMIT 10;"
    execute_query(second_query)
