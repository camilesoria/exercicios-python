# Exercício que permite cadastrar dois números e selecionar a operação desejada com eles

print("Bem-vindo à Calculadora Simples\n")

resultado = None
continuar = None

def cadastrar_numeros():
    try: # Tenta fazer alguma coisa específica. Se der errado, cai no except.
        if resultado is not None and continuar == 'S': # Se houver resultado e o usuário quiser continuar
            num1 = resultado
            num2 = float(input("Digite o segundo valor: "))
            return num1, num2
        
        else: # Caso contrário, ou primeiro cadastro
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        return num1, num2
    
    except ValueError: # Caso o usuário digite algo que não seja número, pede para cadastrar novamente
        print("Entrada inválida. Por favor, digite números válidos.")
        return cadastrar_numeros() # Essa técnica se chama recursividade. Basicamente, é um loop feito com função até que o que a gente quer que aconteça dê certo.

while True:

    if resultado is not None:
        resultado = int(resultado) if resultado.is_integer() else resultado # Isso se chama "ternary operator" ou "conditional expression"
        # É bom porque reduz as linhas de código necessárias para fazer uma verificação simples.
        # Sua sintaxe é <valor_se_verdadeiro> if <condição> else <valor_se_falso>. Legal né?

        print(f"\nO resultado da última operação foi: {resultado}")
        print("Deseja continuar esta conta ou começar uma nova?")
        continuar = input("Digite 'S' para continuar ou 'N' para nova conta: ").strip().upper()

        num1, num2 = cadastrar_numeros()

    else:
        num1, num2 = cadastrar_numeros()

    print("Escolha a operação desejada: ")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Sair")
    try:
        choice = int(input("\nDigite o número da operação desejada: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite uma opção válida.\n")
        continue

    if choice == 1: # Soma
        resultado = num1 + num2

    elif choice == 2: # Subtração
        resultado = num1 - num2

    elif choice == 3: # Multiplicação
        resultado = num1 * num2


    elif choice == 4: # Divisão
        if num2 != 0: # Verificamos se o divisor não é zero para evitar erro
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida. Voltando ao menu...\n")

    elif choice == 5: # Sair
        print("Encerrando a calculadora. Até mais!")
        break
    
    else:
        print("Erro inesperado. Encerrando a calculadora...\n")

# Dica: Usamos a função is_integer() para verificar se o resultado é um número inteiro.
#  Se for, convertemos para int para evitar exibir números como 5.0. Fica mais bonito assim.