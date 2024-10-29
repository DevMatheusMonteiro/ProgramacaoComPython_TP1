vini = 7000
rodri = 5000
bellingham = 4000
contador = 0
while(contador < 3):
    contador += 1
    voto = int(input("1 - Vini Jr\n2 - Rodri\n3 - Bellingham\nEscolha: "))
    if(voto == 1):
        vini += 1
    elif(voto == 2):
        rodri += 1
    elif(voto == 3):
        bellingham += 1
    else:
        print("Inválido!")
        contador -= 1
print(f"Vini Jr: {vini} votos\nRodri: {rodri} votos\nBellingham: {bellingham} votos")