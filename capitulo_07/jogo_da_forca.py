import random

pergunta = int(input("Digite 1 para sortear a palavra ou 2 para digitar a palavra: "))
lista_de_palavras = ["Teste", "Mesa", "Maca", "Testa", "Apocalipse", "Briga", "Bode", "Computador"]
if pergunta == 1:
    palavra = random.sample(lista_de_palavras, 1)[0].lower().strip()
    print(palavra)
else:
    palavra = input("Digite a palavra secreta: ").lower().strip()

# palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()


digitadas = []
acertos = []
erros = 0
linha2 = ""

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else"."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Voocê já tentou essa letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros == 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 = " /  "
    elif erros == 6:
        linha3 = " / \ "
    print(f"X{linha3}")
    print("X\n==========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break