# Exercício que exibe a tabuada dos números inseridos pelo usuário, repetindo até que o usuário decida parar.

print("Bem-vindo à tabuada interativa!\n")

num = None
continuar = None

while True:
    try:
        num = int(input("Digite um número inteiro para ver sua tabuada: "))

        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print()  # Linha em branco para melhor visualização

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")

    try:
        continuar = input("Deseja ver a tabuada de outro número? (Pressione enter para continuar ou 'N' para sair): ").strip().upper()
        if continuar == 'N':
            print("Obrigado por usar a tabuada interativa. Até a próxima!")
            break # break quebra o loop mais próximo (ou seja, encerra nosso while True)
    except ValueError:
        print("Entrada inválida. Por favor, responda com 'S' ou 'N'.\n")