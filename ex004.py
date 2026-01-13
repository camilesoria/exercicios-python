# Exercício que fará alguns testes e análises em uma variável de entrada

variavel = input("Insira algo: ")

print("Qual o tipo da variável? {}".format(type(variavel))) # Imprime o tipo da variável
print("A variável está em minúsculas? {}".format(variavel.islower())) # Verifica se a variável está em minúsculas
print("A variável está em maiúsculas? {}".format(variavel.isupper())) # Verifica se a variável está em maiúsculas
print("A variável só tem espaços? {}".format(variavel.isspace())) # Verifica se a variável só contém espaços
print("A variável é numérica? {}".format(variavel.isnumeric())) # Verifica se a variável é numérica
print("A variável é alfabética? {}".format(variavel.isalpha())) # Verifica se a variável é alfabética
print("A variável é alfanumérica? {}".format(variavel.isalnum())) # Verifica se a variável é alfanumérica
print("A variável está capitalizada? {}".format(variavel.istitle())) # Verifica se a variável está capitalizada

if len(variavel) > 0:
    print("A variável contém {} caracteres.".format(len(variavel))) # Imprime o número de caracteres na variável