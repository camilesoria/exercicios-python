# Exercício que verifica se a pessoa já é maior de idade, e, caso sim, há quanto tempo, ou quanto tempo falta para atingir a maioridade

nascimento = int(input("Por favor, insira o seu ano de nascimento: "))
anoAtual = int(input("Agora, insira o ano atual: "))

idade = anoAtual - nascimento

if idade >= 18:
    print("Você já é maior de idade.")
    print(f"Você tem {idade} anos.")
    print(f"Já se passaram {idade - 18} anos desde que você atingiu a maioridade.")
else:
    print("Você ainda não é maior de idade.")
    print(f"Você tem {idade} anos.")
    print(f"Faltam {18 - idade} anos para você atingir a maioridade.")