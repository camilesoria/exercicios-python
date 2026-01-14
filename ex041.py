# Exercício que verifica a idade de um atleta e o classifica em categorias conforme a idade

print("Bem-vindo ao sistema de classificação de atletas!\n")

nascimento = int(input("Por favor, insira o ano de nascimento do atleta: "))
anoAtual = int(input("Agora, insira o ano atual: "))

idade = anoAtual - nascimento

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Júnior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print("O atleta tem {} anos e está na categoria {}.".format(idade, categoria))