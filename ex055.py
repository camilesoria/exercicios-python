# Exercício que lê o peso de cinco pessoas e mostra qual foi o maior e o menor peso lidos

print("Bem-vindo ao verificador de peso!\n")

for c in range(1, 5 + 1):
    peso = float(input(f"Digite o peso da {c}ª pessoa (em kg): ")) # Lemos o peso a cada iteração
    if c == 1:
        maior = peso  # Inicializa a variável maior na primeira iteração. Depois, vamos comparar os outros pesos com ela
        menor = peso  # Fazemos o mesmo aqui
    if peso > maior:
        maior = peso  # Atualiza o maior peso se o peso atual for maior
    elif peso < menor:
        menor = peso  # Atualiza o menor peso se o peso atual for menor

print(f"\nO maior peso lido foi {maior} kg")
print(f"O menor peso lido foi {menor} kg")