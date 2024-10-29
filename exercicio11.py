import random
numJogadas = int(input("Escolha quantas jogadas deseja realizar: "))
for jogada in range(numJogadas):
    print(f"{jogada}º jogada: {int(random.random() * 6 + 1)}")