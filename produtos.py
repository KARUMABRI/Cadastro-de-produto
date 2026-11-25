
from conexao import conexao

def cadastrar_produtos():
    produto = input("Nome do produto: ")
    sku = input("SKU: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")

    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos (nome, SKU, Preco, Quantidade)
    VALUES (%s, %s, %s, %s)
    """

    valores = (produto, sku, preco, quantidade)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto cadastrado com sucesso!")

    cursor.close()
