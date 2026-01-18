# Exercício que exibe um contador regressivo na tela. Um protótipo de timer?

from time import sleep

print("Bem-vindo ao meu timer regressivo!\n")
print("Para começar, escolha quanto tempo você deseja que o timer conte para você.")
print("1. Segundos")
print("2. Minutos")
print("3. Horas")
print("4. Sair")
opcao = int(input("Digite o número correspondente à sua escolha: "))

while opcao not in [1, 2, 3, 4]:
    print("Opção inválida! Por favor, escolha 1, 2, 3 ou 4.")
    opcao = int(input("Digite o número correspondente à sua escolha: "))

if opcao == 1:
    tempo = int(input("Quantos segundos você deseja contar?"))
    total_segundos = tempo # Apenas para manter a consistência

# C é o contador. Ele vai começar em 0 e ir até total_segundos
# Usamos + 1 porque o computador sempre começa a contar do zero, e queremos que fique bonitinho pro usuário
    for c in range(0, total_segundos + 1):
        print(f"{total_segundos - c}")
        sleep(1) # Ele "dorme" por 1 segundo antes de continuar o loop. Assim, parece que ele está contando segundo por segundo
    print("Fim do timer!")

elif opcao == 2:
    tempo = int(input("Quantos minutos você deseja contar?"))
    total_segundos = tempo * 60 # Aqui multipplicamos por 60 para converter minutos em segundos

    for c in range(0, total_segundos + 1):
        print(f"{(total_segundos - c) // 60}:{(total_segundos - c) % 60:02d}")
        # Aqui usamos // pra saber quantos minutos "cabem" dentro dos segundos restantes
        # Usamos % pra pegar o resto da divisão, que são os segundos restantes
        # :02d é o que faz aparecer dois dígitos, pra ficar mais bonitinho (ex: 5:03 em vez de 5:3)
        sleep(1)
    print("Fim do timer!")

elif opcao == 3:
    tempo = int(input("Quantas horas você deseja contar?"))
    total_segundos = tempo * 3600 # Multiplicamos por 3600 porque 1 hora tem 60 minutos e cada minuto tem 60 segundos (60 * 60 = 3600)

    for c in range(0, total_segundos + 1):
        # Esse aqui é quase a mesma coisa. A diferença é que primeiro vemos quantas horas "cabem" dentro dos segundos restantes
        # Depois, pegamos o resto da divisão por 3600 para ver quantos minutos cabem dentro dos segundos restantes
        # E por fim, pegamos o resto da divisão por 60 para ver quantos segundos sobraram
        horas = (total_segundos - c) // 3600
        minutos = ((total_segundos - c) % 3600) // 60
        segundos = (total_segundos - c) % 60
        print(f"{horas}:{minutos:02d}:{segundos:02d}") # O :02d repete pra deixar mais bonito
        sleep(1)
    print("Fim do timer!")

elif opcao == 4:
    print("Saindo do programa. Até mais!")

else:
    print("Erro inesperado. Encerrando o programa.")

    # Dica: Se quiser que o terminal fique mais limpo, adicione no final dos prints ", end='\r'" (sem aspas)
    # Isso faz com que a próxima impressão sobrescreva a anterior, ao invés de criar uma nova linha, deixando o terminal lindinho