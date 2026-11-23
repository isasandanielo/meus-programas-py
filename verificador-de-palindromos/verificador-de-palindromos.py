frase = str(input("Digite uma frase: ")).replace(" ", "").upper()
frase_invertida = ""
for letra in frase:
    if letra != " ":
        frase_invertida = letra + frase_invertida
if frase == frase_invertida:
    print(f"A frase: {frase} é um palíndromo!")
else:
    print(f"A frase: {frase} não um palíndromo!")