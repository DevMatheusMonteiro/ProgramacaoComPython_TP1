minutosFornecidos = int(input("Informe os minutos: "))
horas = int(minutosFornecidos / 60)
minutos = minutosFornecidos % 60
print(f"{str(horas).rjust(2,'0')}:{str(minutos).rjust(2,'0')}")
horasConvertidaParaMinutosTotais = horas * 60
horasConvertidaParaMinutosTotais += minutos
print(horasConvertidaParaMinutosTotais)