
from produtos import (
    cadastrar_produtos,
    listar_produtos,
    atualizar_produto,
    pesquisar_produto,
    excluir_produto
)

while True:
    print("\n========== SISTEMA DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Pesquisar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair")
    print("========================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        pesquisar_produto()

    elif opcao == "4":
        atualizar_produto()

    elif opcao == "5":
        excluir_produto()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
