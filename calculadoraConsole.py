# Exercício que realiza operações com dois ou mais números

print("Bem-vindo à Calculadora de Console!\n")

numero1 = float(input("Digite o primeiro número: "))
while True:
    operacao = int(input("Digite a operação desejada:\n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n5.Potenciação \n6. Raiz Quadrada  \nOpção:"))
    if operacao in [1, 2, 3, 4, 5]:
        numero2 = float(input("Digite o próximo número: "))

        if operacao == 1: # Soma
                resultado = numero1 + numero2

        elif operacao == 2: # Subtração
                resultado = numero1 - numero2

        elif operacao == 3: # Multiplicação
                resultado = numero1 * numero2

        elif operacao == 4: # Divisão
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue

        elif operacao == 5: # Potenciação
                resultado = numero1 ** numero2

    elif operacao == 6: # Raiz Quadrada
            resultado = numero1 ** 0.5

    print(f"Resultado: {resultado}")
    continuar = input("Deseja continuar a operação com o resultado atual? (s/n): ").lower()
    if continuar == 's':
        numero1 = resultado
    else:
        print(f"Certo! Seu resultado final é: {resultado}")
        break

    if operacao not in [1, 2, 3, 4, 5, 6]:
        print("Operação inválida. Por favor, escolha uma operação válida.")