# Exercício que lê idade e sexo de várias pessoas, mostrando no final quantas pessoas têm mais de 18 anos, quantos homens foram cadastrados e quantas mulheres têm menos de 20 anos.

print("Bem-vindo ao sistema de cadastro de pessoas!\n")

pessoas = 0
maiores = 0
homens = 0
mulheres_menos_20 = 0

while True:
    try:
        idade = int(input("Digite a idade da pessoa:\n"))
        genero = input("Digite o gênero da pessoa (M/F):\n").strip().upper()
    except ValueError:
        print("Entrada inválida. Por favor, insira valores válidos.\n")
        continue

    pessoas += 1

    if genero not in ['M', 'F']:
        print("Gênero inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.\n")
        continue

    if idade >= 18:
        maiores += 1

    if genero == "M":
        homens += 1 
    
    elif genero == "F" and idade < 20:
        mulheres_menos_20 += 1

    print("Pessoa cadastrada com sucesso!\n")
    
    continuar = input("Deseja cadastrar outra pessoa? (Digite enter para continuar ou 'N' para sair): ").strip().upper()

    if continuar == 'N':
        print("-"*30) # Apenas um separador visual para melhor organização no terminal
        print(f"\nTotal de pessoas cadastradas: {pessoas}")
        print(f"Total de pessoas com mais de 18 anos: {maiores}")
        print(f"Total de homens cadastrados: {homens}")
        print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}\n")
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("-"*30) # Mesmo caso do separador visual acima