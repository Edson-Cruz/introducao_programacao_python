linha_01 = [7, 8, 9]
linha_02 = [4, 5, 6]
linha_03 = [1, 2, 3]
numeros_jogados = []
marca_jogador_01 = ""
marca_jogador_02 = ""

# Verificando a entrada de dados do usuários
while True:
    marca_jogador_01 = input("Deseja jogar com O ou X: ").upper().strip()
    print("-------------------------------\n"
          f"Jogador 01 - {marca_jogador_01}")

    if marca_jogador_01 != "X".upper().strip() and marca_jogador_01 != "O".upper().strip():
        print("Digite X ou O para continuar!")
    if marca_jogador_01 == "X":
        marca_jogador_02 = "O".upper().strip()
        print(f"Jogador 02 - {marca_jogador_02}"
               "\n-------------------------------")
        break
    elif marca_jogador_01 == "O":
        marca_jogador_02 = "X".upper().strip()
        print(f"Jogador 02 - {marca_jogador_02}"
               "\n-------------------------------")
        break


print("\n 7 | 8 | 9 \n"
      "---+---+---\n"
      " 4 | 5 | 6 \n"
      "---+---+---\n"
      " 1 | 2 | 3 \n")

# Iniciando o jogo e o jogador 1
while True:
    jogada_jogador_01 = int(input("Jogador 1 - Selecione a posição que deseja jogar: "))
    if (1 <= jogada_jogador_01 <= 3) and (jogada_jogador_01 in numeros_jogados):
        while jogada_jogador_01 in numeros_jogados:
            jogada_jogador_01 = int(input("Jogador 1 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_01 <= 3) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_03[jogada_jogador_01 - 1] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_01 <= 6) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_02[jogada_jogador_01 - 4] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_01 <= 9) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_01[jogada_jogador_01 - 7] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (1 <= jogada_jogador_01 <= 3) and (jogada_jogador_01 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_01)
        linha_03[jogada_jogador_01 - 1] = marca_jogador_01
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    elif (4 <= jogada_jogador_01 <= 6) and (jogada_jogador_01 in numeros_jogados):
        while jogada_jogador_01 in numeros_jogados:
            jogada_jogador_01 = int(input("Jogador 1 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_01 <= 3) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_03[jogada_jogador_01 - 1] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_01 <= 6) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_02[jogada_jogador_01 - 4] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_01 <= 9) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_01[jogada_jogador_01 - 7] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (4 <= jogada_jogador_01 <= 6) and (jogada_jogador_01 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_01)
        linha_02[jogada_jogador_01 - 4] = marca_jogador_01
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    elif (7 <= jogada_jogador_01 <= 9) and (jogada_jogador_01 in numeros_jogados):
        while jogada_jogador_01 in numeros_jogados:
            jogada_jogador_01 = int(input("Jogador 1 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_01 <= 3) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_03[jogada_jogador_01 - 1] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_01 <= 6) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_02[jogada_jogador_01 - 4] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_01 <= 9) and (jogada_jogador_01 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_01)
                linha_01[jogada_jogador_01 - 7] = marca_jogador_01
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (7 <= jogada_jogador_01 <= 9) and (jogada_jogador_01 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_01)
        linha_01[jogada_jogador_01 - 7] = marca_jogador_01
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    else:
        print("Selecione uma posição entre 1 e 9!")
    
    # Verificando os valores das colunas e do X
    coluna_01 = [linha_01[0], linha_02[0], linha_03[0]]
    coluna_02 = [linha_01[1], linha_02[1], linha_03[1]]
    coluna_03 = [linha_01[2], linha_02[2], linha_03[2]]
    xis_01 = [linha_01[0], linha_02[1], linha_03[2]]
    xis_02 = [linha_01[2], linha_02[1], linha_03[0]]

    # Verificando a vitória do jogador 1
    if (linha_01.count(marca_jogador_01) == 3) or (linha_02.count(marca_jogador_01) == 3) or (linha_03.count(marca_jogador_01) == 3):
        print("\nParabéns Jogador 1, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!\n")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break
    elif (coluna_01.count(marca_jogador_01) == 3) or (coluna_02.count(marca_jogador_01) == 3) or (coluna_03.count(marca_jogador_01) == 3):
        print("\nParabéns Jogador 1, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break
    elif (xis_01.count(marca_jogador_01) == 3) or (xis_02.count(marca_jogador_01) == 3):
        print("\nParabéns Jogador 1, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break

    # Parando o jogo caso não haja vitória (Empate)
    if len(numeros_jogados) == 9:
        print("Não houve um jogador vencedor!")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break

    # Iniciando o jogador 2
    jogada_jogador_02 = int(input("Jogador 2 - Selecione a posição que deseja jogar: "))
    if (1 <= jogada_jogador_02 <= 3) and (jogada_jogador_02 in numeros_jogados):
        while jogada_jogador_02 in numeros_jogados:
            jogada_jogador_02 = int(input("Jogador 2 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_02 <= 3) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_03[jogada_jogador_02 - 1] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_02 <= 6) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_02[jogada_jogador_02 - 4] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_02 <= 9) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_01[jogada_jogador_02 - 7] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (1 <= jogada_jogador_02 <= 3) and (jogada_jogador_02 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_02)
        linha_03[jogada_jogador_02 - 1] = marca_jogador_02
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    elif (4 <= jogada_jogador_02 <= 6) and (jogada_jogador_02 in numeros_jogados):
        while jogada_jogador_02 in numeros_jogados:
            jogada_jogador_02 = int(input("Jogador 2 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_02 <= 3) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_03[jogada_jogador_02 - 1] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_02 <= 6) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_02[jogada_jogador_02 - 4] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_02 <= 9) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_01[jogada_jogador_02 - 7] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (4 <= jogada_jogador_02 <= 6) and (jogada_jogador_02 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_02)
        linha_02[jogada_jogador_02 - 4] = marca_jogador_02
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    elif (7 <= jogada_jogador_02 <= 9) and (jogada_jogador_02 in numeros_jogados):
        while jogada_jogador_02 in numeros_jogados:
            jogada_jogador_02 = int(input("Jogador 2 - Posição já selecionada! Selecione outra posição: "))
            if (1 <= jogada_jogador_02 <= 3) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_03[jogada_jogador_02 - 1] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (4 <= jogada_jogador_02 <= 6) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_02[jogada_jogador_02 - 4] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
            elif (7 <= jogada_jogador_02 <= 9) and (jogada_jogador_02 not in numeros_jogados):
                numeros_jogados.append(jogada_jogador_02)
                linha_01[jogada_jogador_02 - 7] = marca_jogador_02
                print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
                       "---+---+---\n"
                      f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
                       "---+---+---\n"
                      f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
                break
    elif (7 <= jogada_jogador_02 <= 9) and (jogada_jogador_02 not in numeros_jogados):
        numeros_jogados.append(jogada_jogador_02)
        linha_01[jogada_jogador_02 - 7] = marca_jogador_02
        print(f"\n {linha_01[0]} | {linha_01[1]} | {linha_01[2]}\n"
               "---+---+---\n"
              f" {linha_02[0]} | {linha_02[1]} | {linha_02[2]}\n"
               "---+---+---\n"
              f" {linha_03[0]} | {linha_03[1]} | {linha_03[2]}\n")
    else:
        print("Selecione uma posição entre 1 e 9!")

    # Verificando os valores das colunas e do X
    coluna_01 = [linha_01[0], linha_02[0], linha_03[0]]
    coluna_02 = [linha_01[1], linha_02[1], linha_03[1]]
    coluna_03 = [linha_01[2], linha_02[2], linha_03[2]]
    xis_01 = [linha_01[0], linha_02[1], linha_03[2]]
    xis_02 = [linha_01[2], linha_02[1], linha_03[0]]

    # Verificando a vitória do jogador 2
    if (linha_01.count(marca_jogador_02) == 3) or (linha_02.count(marca_jogador_02) == 3) or (linha_03.count(marca_jogador_02) == 3):
        print("\nParabéns Jogador 2, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!\n")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break
    elif (coluna_01.count(marca_jogador_02) == 3) or (coluna_02.count(marca_jogador_02) == 3) or (coluna_03.count(marca_jogador_02) == 3):
        print("\nParabéns Jogador 2, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break
    elif (xis_01.count(marca_jogador_02) == 3) or (xis_02.count(marca_jogador_02) == 3):
        print("\nParabéns Jogador 2, você ganhou!\n")
        jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
        if jogar_novamente == "SIM".upper().strip():
            linha_01 = [7, 8, 9]
            linha_02 = [4, 5, 6]
            linha_03 = [1, 2, 3]
            numeros_jogados.clear()
            print("\nO jogo será iniciado pelo outro jogador!")
        else:
            print("Jogo encerrado! Obrigado por jogar!")
            break
    
    # Parando o jogo caso não haja vitória (Empate)
    if len(numeros_jogados) == 9:
            print("Não houve um jogador vencedor!")
            jogar_novamente = input("Deseja jogar novamente? Digite SIM ou NÃO: ").upper().strip()
            if jogar_novamente == "SIM".upper().strip():
                linha_01 = [7, 8, 9]
                linha_02 = [4, 5, 6]
                linha_03 = [1, 2, 3]
                numeros_jogados.clear()
                print("\nO jogo será iniciado pelo outro jogador!")
            else:
                print("Jogo encerrado! Obrigado por jogar!")
                break
