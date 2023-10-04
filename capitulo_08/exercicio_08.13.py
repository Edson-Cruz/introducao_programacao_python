def verificar_opcoes(palavra):
    opcoes = ["t", "s"]
    while True:
        p = input(palavra).lower().strip()
        for opcao in opcoes:
            if opcao in p:
                validacao = 1
                continue
            else:
                validacao = 0
                print("Digite novamente outra opção!")
                break
        if validacao == 1:
            print("Válido!")
            break
verificar_opcoes(
    "Digite uma palavra: "
)