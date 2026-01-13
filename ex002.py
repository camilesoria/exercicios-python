# Exercício que recebe nome do usuário e, em seguida imprime uma saudação personalizada.
nome = input("Olá, qual é o seu nome?\n")
print("Olá, " + nome + "! Prazer em conhecer você!\n")

# Também podemos usar o combo "{} +  .format()" para imprimir a variável
print("Olá, {}! Prazer em conhecer você!\n".format(nome))

# Dica: "\n" insere uma quebra de linha, ou seja, pula a próxima linha : )