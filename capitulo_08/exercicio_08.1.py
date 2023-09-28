def maior_numero(numero_um, numero_dois):
    if numero_um > numero_dois:
        return numero_um
    else:
        return numero_dois


numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

print(f"Maior número: {maior_numero(numero_um, numero_dois)}")
