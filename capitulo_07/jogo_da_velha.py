linha_01 = [1, 2, 3]
linha_02 = [4, 5, 6]
linha_03 = [7, 8, 9]
numeros_jogados = []
marca_jogador_01 = ""
marca_jogador_02 = ""

# Verificando a entrada de dados do usuários
while True:
    marca_jogador_01 = input("Deseja jogar com O ou X: ").upper().strip()
    print(f"Jogador 01 - {marca_jogador_01}")

    if marca_jogador_01 != "X".upper().strip() and marca_jogador_01 != "O".upper().strip():
        print("Digite X ou O para continuar!")
    if marca_jogador_01 == "X":
        marca_jogador_02 = "O".upper().strip()
        print(f"Jogador 02 - {marca_jogador_02}")
        break
    elif marca_jogador_01 == "O":
        marca_jogador_02 = "X".upper().strip()
        print(f"Jogador 02 - {marca_jogador_02}")
        break


print("\n 1 | 2 | 3 \n"
      "---+---+---\n"
      " 4 | 5 | 6 \n"
      "---+---+---\n"
      " 7 | 8 | 9 \n")

while True:
    jogada_jogador_01 = int(input("Selecione a posição que deseja jogar: "))
    if 1 <= jogada_jogador_01 <= 3: # Verificando a entrada de dados na primeira linha
        if jogada_jogador_01 not in numeros_jogados: # Verificando se a posição desejada está livre para jogar
            numeros_jogados.append(jogada_jogador_01)
            linha_01[jogada_jogador_01 - 1] = marca_jogador_01
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
    elif 4 <= jogada_jogador_01 <= 6:
        if jogada_jogador_01 not in numeros_jogados:
            numeros_jogados.append(jogada_jogador_01)
            linha_02[jogada_jogador_01 - 4] = marca_jogador_01
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                   "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
    elif 7 <= jogada_jogador_01 <= 9:
        if jogada_jogador_01 not in numeros_jogados:
            numeros_jogados.append(jogada_jogador_01)
            linha_03[jogada_jogador_01 - 7] = marca_jogador_01
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                   "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
            
    jogada_jogador_02 = int(input("Selecione a posição que deseja jogar: "))
    if 1 <= jogada_jogador_02 <= 3: # Verificando a entrada de dados na primeira linha
        if jogada_jogador_02 not in numeros_jogados: # Verificando se a posição desejada está livre para jogar
            numeros_jogados.append(jogada_jogador_02)
            linha_01[jogada_jogador_02 - 1] = marca_jogador_02
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
    elif 4 <= jogada_jogador_02 <= 6:
        if jogada_jogador_02 not in numeros_jogados:
            numeros_jogados.append(jogada_jogador_02)
            linha_02[jogada_jogador_02 - 4] = marca_jogador_02
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                   "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
    elif 7 <= jogada_jogador_02 <= 9:
        if jogada_jogador_02 not in numeros_jogados:
            numeros_jogados.append(jogada_jogador_02)
            linha_03[jogada_jogador_02 - 7] = marca_jogador_02
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                   "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
        else:
            print("Posição já selecionada, jogue em outra posição!\n")
            print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]} \n"
                  "---+---+---\n"
                  f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]} \n"
                   "---+---+---\n"
                  f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]} \n")
    else:
        print(f"{jogada_jogador_01} - Número inválido, digite um número válido!")
        break # Retirar esse break
