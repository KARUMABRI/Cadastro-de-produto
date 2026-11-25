import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empresa"
)

if conexao.is_connected():
    print("Conexão bem-sucedida ao banco de dados!")    