# Exercício que calcula o fatorial de um número fornecido pelo usuário

print("Bem-vindo à calculadora de Fatorial!\n")

fatorial = 1

try:
    num = int(input("Digite um número inteiro não negativo para calcular seu fatorial: "))

    if num< 0:
        print("Entrada inválida. Por favor, digite um número inteiro não negativo.")
        exit()
    
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro não negativo.")
    exit()

while num > 0:

    if fatorial != 1: # Não faz sentido mostrar 1 * num, então só mostramos a partir do segundo passo
        print(f"{fatorial} * {num} = {fatorial * num}")

    fatorial *= num
    num -= 1

print(f"O fatorial do número inserido é: {fatorial}")