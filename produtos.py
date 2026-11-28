
from conexao import conectar
from validacoes import obter_texto, obter_inteiro, obter_preco


def exibir_produto(produto):
    print("-------------------------")
    print(f"ID: {produto[0]}")
    print(f"SKU: {produto[1]}")
    print(f"Nome: {produto[2]}")
    print(f"Preço: R$ {produto[3]:.2f}")
    print(f"Quantidade: {produto[4]}")



def cadastrar_produtos():
    produto = obter_texto("Nome do produto: ")
    sku = obter_inteiro("SKU: ", minimo=1)
    preco = obter_preco("Preço: ")
    quantidade = obter_inteiro("Quantidade: ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        sql = """
        INSERT INTO produtos (nome, sku, preco, quantidade)
        VALUES (%s, %s, %s, %s)
        """

        valores = (produto, sku, preco, quantidade)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Produto cadastrado com sucesso!")

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao cadastrar produto: {erro}")

    finally:
        cursor.close()
        conexao.close()


def listar_produtos():
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        sql = "SELECT * FROM produtos"

        cursor.execute(sql)
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in produtos:
            exibir_produto(produto)

    except Exception as erro:
        print(f"Erro ao listar produtos: {erro}")

    finally:
        cursor.close()
        conexao.close()


def pesquisar_produto():
    nome = obter_texto("Digite o nome do produto: ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        sql = """
        SELECT * FROM produtos
        WHERE nome LIKE %s
        """

        valores = (f"%{nome}%",)

        cursor.execute(sql, valores)
        produtos = cursor.fetchall()

        if produtos:
            for produto in produtos:
                exibir_produto(produto)
        else:
            print("Nenhum produto encontrado.")

    except Exception as erro:
        print(f"Erro ao pesquisar produto: {erro}")

    finally:
        cursor.close()
        conexao.close()


def atualizar_produto():
    nome = obter_texto("Digite o nome do produto que deseja atualizar: ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        sql = "SELECT * FROM produtos WHERE nome LIKE %s"

        cursor.execute(sql, (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Produto não encontrado.")
            return

        for produto in produtos:
            exibir_produto(produto)

        id_produto = obter_inteiro(
            "Digite o ID do produto que deseja atualizar: ",
            minimo=1
        )

        ids_encontrados = [produto[0] for produto in produtos]

        if id_produto not in ids_encontrados:
            print("Esse ID não pertence aos produtos encontrados.")
            return

        nome_novo = obter_texto("Novo nome: ")
        preco = obter_preco("Novo preço: ")
        quantidade = obter_inteiro("Nova quantidade: ", minimo=0)

        print("\n--- CONFIRME AS ALTERAÇÕES ---")
        print(f"Novo nome: {nome_novo}")
        print(f"Novo preço: R$ {preco:.2f}")
        print(f"Nova quantidade: {quantidade}")

        confirmacao = obter_texto(
            "Deseja salvar essas alterações? (s/n): "
        )

        if confirmacao.lower() != "s":
            print("Atualização cancelada.")
            return

        sql = """
        UPDATE produtos
        SET nome = %s, preco = %s, quantidade = %s
        WHERE id = %s
        """

        valores = (nome_novo, preco, quantidade, id_produto)

        cursor.execute(sql, valores)
        conexao.commit()

        print(f"Linhas alteradas: {cursor.rowcount}")

        if cursor.rowcount > 0:
            print("Produto atualizado com sucesso!")
        else:
            print("Nenhuma alteração realizada. Os dados podem ser iguais aos anteriores.")

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao atualizar produto: {erro}")

    finally:
        cursor.close()
        conexao.close()


def excluir_produto():
    nome = obter_texto("Digite o nome do produto que deseja excluir: ")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    try:
        sql = "SELECT * FROM produtos WHERE nome LIKE %s"

        cursor.execute(sql, (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Produto não encontrado.")
            return

        print("\n--- PRODUTOS ENCONTRADOS ---")

        for produto in produtos:
            exibir_produto(produto)

        id_produto = obter_inteiro("Digite o ID do produto que deseja excluir: ", minimo=1)

        ids_encontrados = [produto[0] for produto in produtos]

        if id_produto not in ids_encontrados:
            print("Esse ID não pertence aos produtos encontrados.")
            return

        confirmacao = obter_texto("Deseja realmente excluir? (s/n): ")

        if confirmacao.lower() != "s":
            print("Exclusão cancelada.")
            return

        sql = "DELETE FROM produtos WHERE id = %s"

        cursor.execute(sql, (id_produto,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Produto excluído com sucesso!")
        else:
            print("Nenhum produto excluído.")

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao excluir produto: {erro}")

    finally:
        cursor.close()
        conexao.close()

