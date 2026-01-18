# Exercício que lê o gênero de uma pessoa e valida a entrada, solicitando que repita até que seja fornecido um valor correto.

genero = input("Digite o gênero da pessoa (M/F): ").strip().upper()
# strip() remove espaços em branco antes e depois da string. Lembra o que  upper() faz?

while genero not in('M', 'F'): # Enquanto o gênero não estiver em 'M' ou 'F', repete a solicitação
    print("Gênero inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
    genero = input("Digite o gênero da pessoa (M/F): ").strip().upper()