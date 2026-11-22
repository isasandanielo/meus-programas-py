total = maiores_mil = 0
mais_barato = produto = str(input("Nome do produto: "))
preco_mais_barato = preco = float(input("Preço do produto: "))
while True:
    total += preco
    continuar = str(input("Deseja continuar? [S/N]")).upper()[:1]
    while continuar not in('S', 'N'):
        print("Opção inválida!")
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[:1]
    if continuar == 'N':
        break    
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    if preco < preco_mais_barato:
        mais_barato = produto
        preco_mais_barato = preco
    if preco > 1000.00:
        maiores_mil += 1
print("Total gasto: ", total)
print("Quantidade de produtos acima de R$1000.00: ", maiores_mil)
print("Produto mais barato: ", mais_barato)