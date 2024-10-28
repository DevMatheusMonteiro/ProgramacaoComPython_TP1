altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em  quilogramas: "))
imc = peso / (altura ** 2)
print(f"IMC de {imc}")
if(imc < 18.5):
    print("Baixo peso")
elif(imc < 25):
    print("Normal")
elif(imc < 30):
    print("Sobrepeso")
else:
    print("Obesidade")