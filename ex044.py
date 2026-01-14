# Exercício que calcula o preço a ser pago dependendo o método de pagamento escolhido

def dinheiroCheque(preco):
    preco = preco - (preco * 0.1)
    return preco

def cartaoVista(preco):
    preco = preco - (preco * 0.05)
    return preco

def cartaoParcelado(preco):
    preco = preco + (preco * 0.2)
    return preco

print("Bem-vindo ao sistema de cálculo de preços!\n")

preco = float(input("Por favor, insira o preço do produto: R$ "))   
print("Escolha a forma de pagamento:") 
print("1 - À vista em dinheiro ou cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")
opcao = int(input("Digite o número correspondente à sua escolha: "))


if opcao == 1:
    preco_final = dinheiroCheque(preco)
    print("Preço final com desconto: R$ {:.2f}".format(preco_final))

elif opcao == 2:
    preco_final = cartaoVista(preco)
    print("Preço final com desconto: R$ {:.2f}".format(preco_final))

elif opcao == 3:
    preco_final = preco
    print("Preço final sem desconto: R$ {:.2f}".format(preco_final))

elif opcao == 4:
    preco_final = cartaoParcelado(preco)
    print("Preço final com juros: R$ {:.2f}".format(preco_final))