lista = [10, 20, 25, 30]

def soma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

print(f"Soma: {soma(lista)}")
print(f"Soma de outra lista: {soma(lista=[1, 2, 3])}")
