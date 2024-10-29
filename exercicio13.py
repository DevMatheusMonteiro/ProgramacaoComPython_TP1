palavra = input("Escreva: ")
palavra_invertida = palavra[::-1]
palindromo = palavra == palavra_invertida
print(f"{"É um palíndromo" if palindromo else "Não é um palíndromo" }")