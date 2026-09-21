frutas = []

for i in range(3):
    fruta = str(input("Informe qual é a fruta: "))
    frutas.append(fruta)

print(frutas)

frutas.append("uva")
frutas.remove(frutas[1])

for fruta in frutas:
    print(fruta)