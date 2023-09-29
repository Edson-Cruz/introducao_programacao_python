lista = [10, 20, 25, 30]

valor = int(input("Digite o valor a ser pesquisado: "))

def pesquisar_posicao(lista, valor):
    for i, v in enumerate(lista):
        if valor == v:
            return i

print(f"Posição do valor pesquisado: {pesquisar_posicao(lista, valor)}")
