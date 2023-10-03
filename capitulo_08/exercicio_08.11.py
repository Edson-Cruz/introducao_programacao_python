def verificar_string(palavra, minimo, maximo):
    while True:
        p = input(palavra)
        min = int(input(minimo))
        max = int(input(maximo))
        if type(p) != str or type(min) != int or type(max) != int:
            print("Valor inválido! Digite outro valor: ")
            pass
        else:
            if int(len(p)) < min or int(len(p)) > max:
                print(f"Valor inválido! Digite um valor entre {min} e {max}.")
                pass
            else:
                print(f"Valor digitado corretamente: {p} (Tamanho: {len(p)})")
                break


verificar_string(
    "Digite uma palavra: ",
    "Digite o valor mínimo de caracteres: ",
    "Digite o valor máximo de caracteres: "
)
