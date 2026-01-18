# Exercício que registra duas notas de um aluno, calcula a média e informa se o aluno foi aprovado, reprovado ou está de recuperação
# Dica: A vantagem de criar uma função é que, caso tenhamos que mudar o programa ou corrigir um bug depois, podemos fazer isso em um único local

def media(n1, n2): # Criamos uma função que calcula a média entre duas notas
    media = (n1 + n2) / 2
    return media

def situacao(media): # Criamos uma função que determina a situação do aluno com base na média
    if media < 5.0:
        return "Reprovado"
    elif media < 7.0:
        return "Recuperação"
    else:
        return "Aprovado"

print("Bem-vindo ao sistema de avaliação escolar!\n")

nome = str(input("Por favor, insira o nome do aluno: "))
nota1 = float(input(f"Insira a primeira nota de {nome}: "))
nota2 = float(input(f"Insira a segunda nota de {nome}: "))

media_final = media(nota1, nota2) # Aqui, nós chamamos a função e salvamos o resultado dela na variável media. Precisamos fazer isso pra poder usar o resultado depois
situacao_final = situacao(media_final)

if situacao_final == "Reprovado":
    print(f"A média de {nome} é {media_final:.1f}. Infelizmente, {nome} foi reprovado.")
elif situacao_final == "Recuperação":
    print(f"A média de {nome} é {media_final:.1f}. {nome} está de recuperação.")
elif situacao_final == "Aprovado":
    print(f"A média de {nome} é {media_final:.1f}. Parabéns, {nome} foi aprovado!")
else:
    print("Erro inesperado. Encerrando o programa.")

# Dica: Eu cometi um erro no commit anterior. Nunca dê o mesmo nome para uma variável e para uma função.
# Isso se chama Variable Shadowing e pode causar erros difíceis de detectar.
# O Python pode ver o nome e não saber se você está se referindo à variável ou à função.