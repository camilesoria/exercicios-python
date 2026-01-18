# Exercício que fará alguns testes e análises em uma variável de entrada

variavel = input("Insira algo: ")

print(f"Qual o tipo da variável? {type(variavel)}") # Imprime o tipo da variável
print(f"A variável está em minúsculas? {variavel.islower()}") # Verifica se a variável está em minúsculas
print(f"A variável está em maiúsculas? {variavel.isupper()}") # Verifica se a variável está em maiúsculas
print(f"A variável só tem espaços? {variavel.isspace()}") # Verifica se a variável só contém espaços
print(f"A variável é numérica? {variavel.isnumeric()}") # Verifica se a variável é numérica
print(f"A variável é alfabética? {variavel.isalpha()}") # Verifica se a variável é alfabética
print(f"A variável é alfanumérica? {variavel.isalnum()}") # Verifica se a variável é alfanumérica
print(f"A variável está capitalizada? {variavel.istitle()}") # Verifica se a variável está capitalizada

if len(variavel) > 0:
    print(f"A variável contém {len(variavel)} caracteres.") # Imprime o número de caracteres na variável