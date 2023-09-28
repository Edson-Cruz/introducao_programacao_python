def e_multiplo(numero_um, numero_dois):
    if numero_um % numero_dois == 0:
        return True
    else:
        return False
    

numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

print(f"Resultado: {e_multiplo(numero_um, numero_dois)}")
