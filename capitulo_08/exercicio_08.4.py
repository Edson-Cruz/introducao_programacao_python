def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


base = int(input("Digite o valor da base do triângulo: "))
altura = int(input("Digite o valor da altura do triângulo: "))

print(f"A área do triângulo: {area_triangulo(base, altura)}")
