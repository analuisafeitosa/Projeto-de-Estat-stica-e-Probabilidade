import sqlite3

# Nome do arquivo .txt e do banco de dados
data_file = 'LAT.txt'
sqlite_db = './db/IoT.db'

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Criar a tabela para armazenar os valores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_values (
        value REAL
    )
''')

# Ler o arquivo .txt e inserir os dados no banco de dados
with open(data_file, 'r') as file:
    for line in file:
        value = (line.strip())
        cursor.execute('INSERT INTO data_values (value) VALUES (?)', (value,))

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()

print()
