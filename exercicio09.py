valor = float(input("Informe o valor da compra: "))
if(valor >= 100):
    if(valor < 200):
        valor *= 1 - 0.1
    elif(valor < 500):
        valor *= 1 - 0.15
    else:
        valor *= 1 - 0.25
print(f"Valor com desconto é: {valor}")