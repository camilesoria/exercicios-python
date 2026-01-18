# Exercício que lê seis números inteiros e mostra a soma apenas dos números pares

print("Bem-vindo à calculadora de soma de números pares! Apesar desse nome ser bem ruim...\n")

soma = 0  # Inicializa a variável soma fora do loop

for c in range(1, 6 + 1):

    num = int(input(f"Digite o {c}º número inteiro: ")) # Lemos um número a cada iteração

    if num % 2 == 0:
        soma += num  # Adiciona o número par à soma. Usar += é uma forma curta de escrever variavel1 = variavel1 + variavel2

    elif num % 2 != 0:
        print("Esse número não me pareceu muito par...")
        continue  # Se o número for ímpar, pula para a próxima iteração

print(f"A soma dos números PARES é {soma}!")