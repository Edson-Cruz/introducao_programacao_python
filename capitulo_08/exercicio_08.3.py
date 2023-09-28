def area_quadrado(lado):
    area = lado ** 2
    return area


lado = int(input("Digite o valor de um lado do quadrado: "))

print(f"A área do quadrado: {area_quadrado(lado)}")
