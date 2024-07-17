import sqlite3


def acessoaobd():
    sqlite_db = "db\IoT.db"

    connection = sqlite3.connect(sqlite_db)

    cursor = connection.cursor() 

    cursor.execute('''
        select *
        from data_values
    ''')
    info = cursor.fetchall()
    return info 