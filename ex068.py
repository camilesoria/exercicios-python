# Exercício que cria um jogo simples de par ou ímpar, que só para quando o usuário perder.

import random # Importamos a biblioteca random para gerar números aleatórios

print("Bem-vindo ao jogo Par ou Ímpar!\n")

while True:
    numero_usuario = int(input("Digite um número inteiro: "))
    try:
        opcao = input("Escolha P para Par ou I para Ímpar: ").strip().upper()

    except ValueError:
        print("Entrada inválida. Por favor, escolha P para Par ou I para Ímpar.\n")
        continue # O loop recomeça e pede as entradas novamente

    numero_computador = random.randint(0, 10) # O computador escolhe um número aleatório entre 0 e 10

    soma = numero_usuario + numero_computador

    if soma % 2 == 0 : # Soma dos números é par

        if opcao == "P": # Usuário escolheu par
            print(f"Você escolheu {numero_usuario}")
            print(f"O computador escolheu {numero_computador}.")
            print(f"A soma é {soma}, que é Par. Você venceu!\n")

        else: # Usuário escolheu ímpar
            print(f"Você escolheu {numero_usuario}")
            print(f"O computador escolheu {numero_computador}.")
            print(f"A soma é {soma}, que é Par. Você perdeu!\n")

            break # Encerra o loop e o jogo

    elif soma % 2 != 0: # Soma dos números é ímpar

        if opcao == "I": # Usuário escolheu ímpar
            print(f"Você escolheu {numero_usuario}")
            print(f"O computador escolheu {numero_computador}.")
            print(f"A soma é {soma}, que é Ímpar. Você venceu!\n")

        else: # Usuário escolheu par
            print(f"Você escolheu {numero_usuario}")
            print(f"O computador escolheu {numero_computador}.")
            print(f"A soma é {soma}, que é Ímpar. Você perdeu!\n")

            break # Encerra o loop e o jogo

    else:
        print("Ocorreu um erro inesperado. Tente novamente.\n")
        continue # Recomeça o loop

    continuar = input("Deseja jogar novamente? (Pressione enter para continuar ou 'N' para sair): ").strip().upper()
    exit() if continuar == 'N' else None