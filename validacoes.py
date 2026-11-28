def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        else:
            print("Entrada inválida. Por favor, insira um texto não vazio.")


def obter_inteiro(mensagem, minimo=0):
    while True:
        try:
            numero = int(input(mensagem))

            if numero < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue

            return numero

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def obter_preco(mensagem):
    while True:
        try:
            valor = input(mensagem).strip()

            preco = float(valor.replace(",", "."))

            if preco < 0:
                print("O preço não pode ser negativo.")
                continue

            return preco

        except ValueError:
            print("Entrada inválida. Digite um preço válido. Exemplo: 15,90")


