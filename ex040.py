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
nota1 = float(input("Insira a primeira nota de {}: ".format(nome)))
nota2 = float(input("Insira a segunda nota de {}: ".format(nome)))

media = media(nota1, nota2) # Aqui, nós chamamos a função e salvamos o resultado dela na variável media. Precisamos fazer isso pra poder usar o resultado depois
situacao = situacao(media)

if situacao == "Reprovado":
    print("A média de {} é {:.1f}. Infelizmente, {} foi reprovado.".format(nome, media, nome))
elif situacao == "Recuperação":
    print("A média de {} é {:.1f}. {} está de recuperação.".format(nome, media, nome))
elif situacao == "Aprovado":
    print("A média de {} é {:.1f}. Parabéns, {} foi aprovado!".format(nome, media, nome))
else:
    print("Erro inesperado. Encerrando o programa.")