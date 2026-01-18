# Exercício que lê números inseridos pelo usuário até que ele digite um valor específico para parar (neste caso, 999)
#  No final, exibe a soma dos números inseridos, excluindo o valor de parada.

print("Bem-vindo ao número secreto!\n")

soma = 0
num = None

while num != 999:
    num = int(input("Digite um número entre 1 e 1000. Se você acertar o número secreto, o jogo termina: "))

    if num == 999:
        break
    else:
        soma += num
    
    print(f"Você digitou o número: {num}")

print(f"A soma dos números inseridos é: {soma}")