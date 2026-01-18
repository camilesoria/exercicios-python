# Exercício que recebe uma frase e verifica se é um palíndromo (lê-se igual de trás para frente), desconsiderando os espaços

print("Bem-vindo ao verificador de palíndromos!\n")

frase = input("Digite uma frase qualquer: ").strip().lower() # Remove espaços e coloca tudo em minúsculas. Isso vai nos ajudar a verificar o palíndromo
frase = frase.replace(" ", "") # Removemos os espaços (" ") e substituimos por nada ("") para facilitar a verificação

for c in range(len(frase) // 2): # Vamos iterar apenas até a metade da frase, porque é o suficiente para verificar o palíndromo
    if frase[c] != frase[-(c + 1)]:
        print("\nA frase NÃO é um palíndromo!")
        break  # Se encontrarmos uma diferença, podemos parar a verificação imediatamente
else:
    print("\nA frase É um palíndromo!")

# Dica: Você sabe que strip() remove espaços. Então, por que usamos replace() também? Pesquise a diferença entre os dois!