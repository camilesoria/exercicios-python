# Exercício que lê o primeiro termo e a razão (o valor a ser somado a cada novo termo) de uma progressão aritmética (PA), e logo exibe os 10 primeiros termos dessa PA
# Similar ao ex051.py, mas com while loop

print("Bem-vindo ao gerador de progressão aritmética!\n")

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

c = 0

while c < 10:
    termo_atual = primeiro_termo + c * razao
    print(f"O {c + 1}º termo da PA é: {termo_atual}")
    c += 1