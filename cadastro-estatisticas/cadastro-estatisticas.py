continuar = " "
maiores = mulheres = 0
homem = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()[:1]
    while sexo not in ('F', 'M'):
        print("Opção inválida!")
        sexo = str(input("Sexo [M/F]: ")).upper()[:1]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homem +=1
    if idade < 20 and sexo == 'F':
        mulheres +=1
    continuar = str(input("Deseja continuar [S/N]: ")).upper()[:1]
    while continuar not in ('S', 'N'):
        print("Opção inválida!")
        continuar = str(input("Deseja continuar [S/N]: ")).upper()[:1]
    if continuar == 'N': 
        break
print("============================================\n")
print(f"Foram cadastrado(s) {maiores} pessoa(s) maior(es) de idade")
print(f"Foram cadastrado(s) {homem} homem(ns)")
print(f"Foram cadastrada(s) {mulheres} menor(es) de 20 anos")