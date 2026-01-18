# Exercício no qual o jogador pode jogar Jokenpô contra o computador

import random # Importa a biblioteca random para gerar escolhas aleatórias
print("Bem-vindo ao jogo de Jokenpô!\n")

itens = ["Pedra", "Papel", "Tesoura"] # Lista com as opções do jogo
computador = random.randint(0, 2) # Gera um número aleatório entre 0 e 2 para a escolha do computador

# Dica: Diferentemente de nós, os computadores começam a contar no zero. Por isso, usamos randint(0, 2) para gerar três números

print("Escolha sua jogada:")
print("1 - Pedra\n")
print("2 - Papel\n")
print("3 - Tesoura\n")
jogador = int(input("Digite o número correspondente à sua escolha: ")) - 1 # Fazemos isso pro n´´umero escolhido pelo computador ser igual ao índice da lista

if jogador == computador:
    resultado = "Empate!"
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    resultado = "Você venceu!"
elif(computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    resultado = "O computador venceu!"

print(f"Você escolheu {itens[jogador]} e o computador escolheu {itens[computador]}.")
print(resultado)
