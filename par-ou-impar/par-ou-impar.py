import random
jogador = True
ganhos = 0
while jogador == True: 
    opcao_jogada = str(input("Par ou ímpar: ")).upper()
    while opcao_jogada not in ('PAR','IMPAR','ÍMPAR'):
        print("Opção inválida!")
        opcao_jogada = str(input("Par ou ímpar: ")).upper()
    numero_jogador = int(input("Digite seu número [1 a 10]: "))
    numero_computador = random.randint(1,10)
    jogada = numero_jogador + numero_computador
    print("O computador digitou: ", numero_computador)
    if opcao_jogada == 'PAR' and jogada % 2 == 0:
        print("Você ganhou essa partida! A soma dos números foi: ", jogada, "\n")
        ganhos += 1
        print('=======================================================\n')
    elif opcao_jogada == 'IMPAR' and jogada % 2 == 1: 
        print("Você ganhou essa partida! A soma dos números foi: ", jogada, "\n")
        ganhos += 1
        print('======================================================\n')
    else:
        print('======================================================\n')
        print("Você perdeu a partida! A soma dos números foi: ", jogada)
        break
print(f"Você ganhou {ganhos} partida(s) consecutivas!")