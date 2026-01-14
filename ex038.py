# Exercício que compara dois números e informa qual é o maior ou se são iguais

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior. ")
elif num2 > num1:
    print("O segundo número é maior. ")
elif num1 == num2:
    print("Os dois números são iguais. ")
else:
    print("Erro inesperado. ")