import sqlite3

data_file = 'LAT.txt'
sqlite_db = './db/IoT.db'

conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_values (
        value REAL
    )
''')

def clean_value(value):
    # remove caracteres especiais
    value = value.replace('\ufeff', '').strip()
    return value

with open(data_file, 'r', encoding='utf-8') as file: 
    for line in file:
        line = clean_value(line)
        try:
            value = float(line)
            cursor.execute('INSERT INTO data_values (value) VALUES (?)', (value,))
        except ValueError:
            print(f"Valor inválido encontrado e ignorado: '{line}'")

conn.commit()
conn.close()
