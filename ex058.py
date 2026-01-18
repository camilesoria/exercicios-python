# Exercício que gera um número aleatório entre 1 e 10 e pede ao usuário para adivinhar até acertar.

import random # Importamos a biblioteca random para gerar números aleatórios

print("Bem-vindo ao jogo Guess the Number!")

numero_secreto = random.randint(1, 10) # Usamos randint para gerar um inteiro aleatório entre 1 e 10
guess = None # Usamos isso para inicializar a variável sem atribuir um valor específico
counter = 0
while guess != numero_secreto:
    guess = int(input("Adivinhe um número entre 1 e 10: "))
    counter += 1
    if guess != numero_secreto:
        print("Você errou! Tente novamente.")

print(f"Parabéns! Você acertou o número {numero_secreto} em {counter} tentativas.")