personagens = ["Luffy", "Zoro", "Nami", "Sanji", "Usopp", "Jinbe", "Robin", "Franklin", "Chopper", "Brook"]
acoes = ["cantou", "comeu", "treinou", "estudou"]
lugares = ["Sabaody", "Alabasta", "Marine Ford", "Impel Down", "Skypiea"]
while(True):
    personagem = int(input("1 - Luffy\n2 - Zoro\n3 - Nami\n4 - Sanji\n5 - Usopp\n 6 - Jinbe\n7 - Robin\n8 - Franklin\n9 - Chopper\n10 - Brook\nEscolha o personagem: "))
    if(personagem < 0 or personagem > len(personagens)):
        print("Escolha inválida")
    else:
        print(len(personagens))
        personagem = personagens[personagem - 1]
        break
while(True):
    acao = int(input("1 - Cantou\n2 - Comeu\n3 - Treinou\n4 - Estudou\nEscolha a ação: "))
    if(acao < 0 or acao > len(acoes)):
        print("Escolha inválida")
    else:
        acao = acoes[acao - 1]
        break
while(True):
    lugar = int(input("1 - Sabaody\n2 - Alabasta\n3 - Marine Ford\n4 - Impel Down\n5 - Skypiea\nEscolha o lugar: "))
    if(lugar < 0 or lugar > len(lugares)):
        print("Escolha inválida")
    else:
        lugar = lugares[lugar - 1]
        break
print(f"{personagem} {acao} em {lugar}")