
from conexao import conexao

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    SKU VARCHAR(20),
    Preco DECIMAL(10, 2),
    Quantidade VARCHAR(80)
)
""")

conexao.commit()

print("Tabela criada com sucesso!")

cursor.close()
conexao.close()

