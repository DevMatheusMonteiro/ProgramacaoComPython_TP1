num1 = int(input("Informe o primeiro número: "))
escolha = int(input("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha: "))
num2 = int(input("Informe o segundo número: "))
if(escolha == 1):
    print(f"Soma: {num1 + num2}")
elif (escolha == 2):
    print(f"Subtração: {num1 - num2}")
elif (escolha == 3):
    print(f"Multiplicação: {num1 * num2}")
elif (escolha == 4):
    if(num2 == 0):
        print("Não é possível dividir por 0!")
    else:
        print(f"Divisão: {num1 / num2}")
else:
    print("Escolha inválida!!")