# Exercício que lê o nome e o preço de vários produtos, mostrando no final qual o valor total gasto na compra, quantos produtos custam mais de R$1000 e qual é o nome do produto mais barato.
print("Bem-vindo ao sistema de cadastro de produtos!\n")

produtos = 0
preco_total = 0
produtos_mais_1000 = 0
produto_mais_barato = None
preco_mais_barato = None

while True:
    try:
        nome = input("Digite o nome do produto:\n").strip()
        preco = float(input("Digite o preço do produto:\n"))

        if preco < 0: # Nunca vi um mercado que pague o cliente para levar um produto!
            print("O preço não pode ser negativo. Por favor, insira um valor válido.\n")
            continue

    except ValueError:
        print("Entrada inválida. Por favor, insira valores válidos.\n")
        continue

    produtos += 1

    if preco > 1000:
        produtos_mais_1000 += 1

    preco_total += preco

    if produtos == 1 or preco < preco_mais_barato:
        produto_mais_barato = nome
        preco_mais_barato = preco

    print("Produto cadastrado com sucesso!\n")
    
    continuar = input("Deseja cadastrar outro produto? (Digite enter para continuar ou 'N' para sair): ").strip().upper()

    if continuar == 'N':
        print("-"*30) # Apenas um separador visual para melhor organização no terminal
        print(f"\nTotal de produtos cadastrados: {produtos}")
        print(f"Total de produtos com preço acima de R$1000: {produtos_mais_1000}")
        print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})\n")
        print(f"Valor total gasto: R$ {preco_total:.2f}\n")
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("-"*30) # Mesmo caso do separador visual acima

        # Dica: Compare esse código com o do ex069.py. Eles não são praticamente a mesma coisa?
        # Na programação, muitas vezes usamos a mesma estrutura ou lógica pra resolver coisas diferentes.
        # Por mais simples que um código pareça, ele pode ser a solução de um grande problema! :)