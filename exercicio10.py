import random
personagens = ["Luffy", "Zoro", "Nami", "Sanji", "Usopp", "Jinbe", "Robin", "Franklin", "Chopper", "Brook"]
acoes = ["cantou", "comeu", "treinou", "estudou"]
lugares = ["Sabaody", "Alabasta", "Marine Ford", "Impel Down", "Skypiea"]
personagem = personagens[int(random.random() * len(personagens))]
acao = acoes[int(random.random() * len(acoes))]
lugar = lugares[int(random.random() * len(lugares))]
print(f"{personagem} {acao} em {lugar}")