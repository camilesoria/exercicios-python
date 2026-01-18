# Exercício que recebe o valor de uma cassa, salário mensal e anos para pagar, e em seguida, decide se o empréstimo será aprovado ou negado
# Caso o valor da parcela mensal seja maior do que 30% do salário mensal, o empréstimo será negado

def emprestimo(preco, salario, anos): # Criamos uma função que verifica o valor da parcela mensal de empréstimo e determina se excede o limite de 30% do salário mensal
    parcela = preco / (anos * 12)
    if parcela > (salario * 0.3): # Verifica se parcela é maior que salario * 0.3 (ao multiplicar por 0.3, conseguimos calcular 30% do salário)
        return f"Empréstimo negado! O valor da parcela mensal R$ {parcela:.2f} excede 30% do seu salário."
    else:
        return f"Empréstimo aprovado! O valor da parcela mensal será de R$ {parcela:.2f}."
    
print("Bem-vindo ao serviço de anállise de empréstimo!\n Para começar, vou precisar de algumas informações: \n")

nome = str(input("Primeiramente, qual é o seu nome? "))

preco = float(input(f"Certo, obrigado {nome}! Agora, me informe o valor da casa que você quer comprar (apenas números): R$ "))
salario = float(input("Perfeito! Agora, me diga quanto você ganha por mês (lembre-se, apenas números) R$ "))
anos = int(input("Excelente! Por fim, me diga em quantos anos você pretende pagar essa casa? "))

resultado = emprestimo(preco, salario, anos)
print(resultado)