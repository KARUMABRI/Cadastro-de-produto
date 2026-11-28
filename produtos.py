
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

def listar_produtos():
    sql = "SELECT * FROM produtos"

    cursor = conexao.cursor()
    cursor.execute(sql)

    produtos = cursor.fetchall()

    for produto in produtos:
        print("-------------------------")
        print(f"ID: {produto[0]}")
        print(f"SKU: {produto[1]}")
        print(f"Nome: {produto[2]}")
        print(f"Preço: R$ {produto[3]:.2f}")
        print(f"Quantidade: {produto[4]}")

def pesquisar_produto():
    nome = input("Digite o nome do produto: ")

    sql = """
    SELECT * FROM produtos
    WHERE nome LIKE %s
    """

    valores = (f"%{nome}%",)

    cursor = conexao.cursor()
    cursor.execute(sql, valores)

    produtos = cursor.fetchall()

    if produtos:
        for produto in produtos:
            print("-------------------------")
            print(f"ID: {produto[0]}")
            print(f"SKU: {produto[1]}")
            print(f"Nome: {produto[2]}")
            print(f"Preço: R$ {produto[3]:.2f}")
            print(f"Quantidade: {produto[4]}")
    else:
        print("Nenhum produto encontrado.")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")

    sql = "SELECT * FROM produtos WHERE nome LIKE %s"
    
    cursor = conexao.cursor()
    cursor.execute(sql, (f"%{nome}%",))
    produtos = cursor.fetchall()

    if not produtos:
        print("Produto não encontrado.")
        return

    for produto in produtos:
        print("-------------------------")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[2]}")
        print(f"Preço: R$ {produto[3]:.2f}")
        print(f"Quantidade: {produto[4]}")

    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))

    nome_novo = input("Novo nome: ")
    preco = float(input("Novo preço: ").replace(".", "").replace(",", "."))
    quantidade = int(input("Nova quantidade: "))

    sql = """
    UPDATE produtos
    SET nome = %s, preco = %s, quantidade = %s
    WHERE id = %s
    """

    valores = (nome_novo, preco, quantidade, id_produto)

    cursor.execute(sql, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhuma alteração realizada.")


def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ")

    sql = "SELECT * FROM produtos WHERE nome LIKE %s"

    cursor = conexao.cursor()
    cursor.execute(sql, (f"%{nome}%",))
    produtos = cursor.fetchall()

    if not produtos:
        print("Produto não encontrado.")
        cursor.close()
        return

    print("\n--- PRODUTOS ENCONTRADOS ---")

    for produto in produtos:
        print("-------------------------")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[2]}")
        print(f"Preço: R$ {produto[3]:.2f}")
        print(f"Quantidade: {produto[4]}")

    id_produto = int(input("Digite o ID do produto que deseja excluir: "))

    ids_encontrados = [produto[0] for produto in produtos]

    if id_produto not in ids_encontrados:
        print("Esse ID não pertence aos produtos encontrados.")
        cursor.close()
        return

    confirmacao = input("Deseja realmente excluir? (s/n): ")

    if confirmacao.lower() != "s":
        print("Exclusão cancelada.")
        cursor.close()
        return

    sql = "DELETE FROM produtos WHERE id = %s"

    cursor.execute(sql, (id_produto,))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Produto excluído com sucesso!")
    else:
        print("Nenhum produto excluído.")

    cursor.close()
