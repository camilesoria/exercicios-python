# Exercício que exibe todos os números ímpares que são múltiplos de 3 entre 1 e 500.

print("Números ímpares múltiplos de 3 entre 1 e 500:\n")
for c in range(1, 500 + 1):
    if c % 2 != 0: # Caso o resto da divisão por 2 seja diferente de zero, o número é ímpar
        if c % 3 == 0: # Se o resto da divisão por 3 for igual a zero, o número é múltiplo de 3
            print(c, end=' ') # Usamos end=' ' para imprimir tudo na mesma linha, separado por espaço   