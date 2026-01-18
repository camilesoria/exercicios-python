# Exercício que lê vários valores digitados pelo usuário e mostra a média entre eles, além do maior e menor valor inseridos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print("Bem-vindo ao calculador de média, maior e menor valor!\n")

soma = 0
contador = 0
continuar = None

while continuar != 'N':
    try:
        num = float(input("Digite um valor numérico: "))
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        continue

    soma += num
    contador += 1

    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    try:
        continuar = input("Deseja continuar? (S/N): ").strip().upper()
    except:
        print("Entrada inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        continuar = None
        continue

media = soma / contador
print(f"\nA média dos valores inseridos é: {media:.2f}")
print(f"O maior valor inserido foi: {maior:.2f}")
print(f"O menor valor inserido foi: {menor:.2f}")