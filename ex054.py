# Exercício que lê a idade de sete pessoas e mostra quantas são maiores e quantas são menores de idade

print("Bem-vindo ao verificador de maioridade!\n")
ano_atual = int(input("Digite o ano atual: ")) # Se pedirmos o ano atual no código, ele vai ser mais durável. Mas quem sabe usar a biblioteca datetime?

maiores = [] # Aqui criamos uma lista para armazenar as pessoas maiores de idade
menores = [] # E aqui a lista de menores de idade

for c in range(1, 7 + 1):
    nome = input(f"Digite o nome da {c}ª pessoa: ")
    ano_nasc = int(input(f"Digite o ano de nascimento de {nome}: "))
    idade = ano_atual - ano_nasc

    if idade >= 18:
        maiores.append({'nome': nome, 'idade': idade}) # Append adiciona um novo item ao final da lista
     
    else:
        menores.append({'nome': nome, 'idade': idade})

print("\nResultado da verificação de maioridade:\n")

print(f"Pessoas maiores de idade ({len(maiores)}):")
for maior in maiores: # Aqui iteramos sobre cada dicionário na lista de maiores
    print(f"-> {maior['nome']} ({maior['idade']} anos)")
    # Usamos maior[chamada_da_chave] para acessar os valores dentro do dicionário
    # "Maior in maiores" é similar ao "for c in range(...)", mas aqui "maior" assume o valor de cada item na lista "maiores" a cada iteração

print(f"Pessoas menores de idade ({len(menores)}):")
for menor in menores:
    print(f"-> {menor['nome']} ({menor['idade']} anos)")