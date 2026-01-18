# Exercício que calcula o IMC de uma pessoa e informa sua classificação conforme o valor obtido

print("Bem-vindo ao sistema de cálculo do IMC!\n")

peso = float(input("Por favor, insira o seu peso em kg: "))
altura = float(input("Agora, insira a sua altura em metros: "))
imc = peso / (altura**2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso ideal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 40: 
    classificacao = "Obesidade"
elif imc >= 40:
    classificacao = "Obesidade mórbida"
else:
    classificacao = "Erro inesperado. Encerrando o programa."

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}.")