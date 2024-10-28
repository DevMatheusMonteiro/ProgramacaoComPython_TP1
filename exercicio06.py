numSecreto = 7
numEscolhido = int(input("Escolha um número para adivinhar o número secreto: "))
resultado = numEscolhido - numSecreto
if (resultado == 0):
    print("Parabéns, adivinhou!")
elif(resultado == -1):
    print("Quase, tente um número um pouco mais alto")
elif (resultado < -1):
    print("Muito baixo, tente um número maior")
elif(resultado == 1):
    print("Quase, tente um número um pouco mais baixo")
elif (resultado > 1):
    print("Muito alto, tente um número menor")
