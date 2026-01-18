# Exercício que converte um número inteiro para binário, hexadecimal ou octal

print("Bem-vindo ao conversor de números!\n")
numero = int(input("Por favor, insira o número que você deseja converter: "))

opcao = int(input("Escolha a base para conversão:\n1 - Binário\n2 - Hexadecimal\n3 - Octal\n4 - Sair\nDigite o número correspondente à sua escolha: "))

# Dica: usamos [2:] para cortar os dois primeiros caracteres das strings retornadas pelas funções de conversão
# Esses dois primeiros caracteres indicam o tipo da base (0b para binário, 0x para hexadecimal e 0o para octal)

if opcao == 1:
    resultado = bin(numero)[2:] # bin() converte para binário
    print(f"O número {numero} em binário é: {resultado}")
elif opcao == 2:
    resultado = hex(numero)[2:] # hex() converte para hexadecimal
    print(f"O número {numero} em hexadecimal é: {resultado}")
elif opcao == 3:
    resultado = oct(numero)[2:] # oct() converte para octal
    print(f"O número {numero} em octal é: {resultado}")
elif opcao == 4:
    print("Saindo do programa. Até mais!")
else:
    while opcao not in [1, 2, 3, 4]:
        print("Opção inválida! Por favor, escolha 1, 2, 3 ou 4.")
        opcao = int(input("Escolha a base para conversão:\n1 - Binário\n2 - Hexadecimal\n3 - Octal\n4 - Sair\nDigite o número correspondente à sua escolha: "))