opcao = 0
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
while opcao != 5:
    print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            print("O resultado da soma dos dois números é: ", num1 + num2) 
        case 2: 
            print("O resultado da multiplicação dos dois números é: ", num1 * num2) 
        case 3:
            if num1 > num2:
                print(f"O número maior é {num1}")
            elif num1 < num2:
                print(f"O número maior é {num2}")
            else: 
                print("Os números são iguais!")
        case 4: 
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
        case 5:
            pass
print("Fim do programa")