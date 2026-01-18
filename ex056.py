# Exercício que lê a idade, nome e gênero de 4 pessoas, e depois exibe a média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos

print("Bem-vindo ao analisador de grupo!\n")
grupo = [] # Inicializando nossa lista vazia
soma = 0 # Como eu usei += depois, preciso inicializar essa variável
F_menos_20 = 0 # Mesma coisa aqui
idade_M_velho = 0 # Pro if funcionar, precisamos inicializar essa variável

for c in range(0, 4+1):
    nome = input(f"Digite o nome da {c + 1}° pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    genero = input(f"Digite o gênero de {nome} (F para feminino/M para masculino): ").upper()
     # Usamos .upper() para garantir que o gênero seja sempre maiúsculo, facilitando as comparações depois
     # Se não fizéssemos isso, teríamos que escrever comparações para 'M', 'm', 'F' e 'f'

    grupo.append({'nome': nome, 'idade': idade, 'genero': genero}) # Adicionamos os dados à nossa lista

print("Cadastro concluído! Vamos começar as análises...")

for pessoa in grupo:
    soma += pessoa['idade']

    if pessoa['genero'] == 'M':

        if pessoa['idade'] > idade_M_velho:
            idade_M_velho = pessoa['idade']
            nom_M_velho = pessoa['nome']

    if pessoa['genero'] == 'F' and pessoa['idade'] < 20: # Se gênero for feminino e idade menor que 20
        F_menos_20 += 1

media = soma // len(grupo) # len(alguma_coisa) retorna o tamanho/comprimento dessa coisa

print("\nAnálises concluídas! Aqui estão os resultados:\n")
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho é {nom_M_velho} com {idade_M_velho} anos")
print(f"Ao todo, são {F_menos_20} mulheres com menos de 20 anos")