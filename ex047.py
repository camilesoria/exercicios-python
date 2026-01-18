# Exercício que mostra todos os números pares de 1 a 50

print("Números pares de 1 a 50:\n")

for n in range(2, 51, 2):
    if n % 2 == 0:
        print(n, end=' ')

print("\nFim da lista!")

# Dica: A estrutura de range() é bem legal. Nesse caso, ela funciona assim:
# range(início, fim, quanto_devo_pular)
# Então, começamos em 2, vamos até 51 (pois o 51 não é incluído) e pulamos de 2 em 2, garantindo que só peguemos os números pares
# Isso economiza processamento, rodando o código 25 vezes ao invés de 50 vezes!