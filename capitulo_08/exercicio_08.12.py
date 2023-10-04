def verificar_lista(palavra, lista):
    p = input(palavra)
    l = lista
    if p in l:
        print(f"{p} está na lista!")
    else:
        print(f"{p} não está na lista!")
verificar_lista(
    "Digite uma palavra: ",
    ["teste", "sair", "casa"]
)