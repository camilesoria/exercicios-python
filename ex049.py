# Exercício que mostra a tabuada de números escolhidos pelo usuário

print("Bem-vindo ao calculador de tabuada!\n")
num = int(input("Digite o número que você deseja ver a tabuada: "))

print("\nTabuada de {}:\n".format(num))
for c in range(0, 10 + 1): # C aumentará desde 0 até 10. Lembra por que usamos 10 + 1?
    resultado = num * c # Armazenamos o resultado em uma variável para exibí-la depois
    print(f"{num} x {c} = {resultado}")

# Dica: Variáveis declaradas e usadas dentro são reescritas a cada iteração do loop
# Então, se precisar daquele valor em outra iteração, armazene-o em uma lista ou outro lugar que não reescreva