multiplicador = range(1,11,1)
tabuada = int(input("Digite um número para ver a tabuada: "))

for i in multiplicador:
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")