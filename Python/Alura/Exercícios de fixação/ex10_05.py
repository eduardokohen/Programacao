frutas = []

for i in range(3):
    fruta = str(input(f"Digite o nome da {i+1}ª fruta: "))
    frutas.append(fruta)

frutas.append("uva")

print()
for fruta in frutas:
    print(fruta)

print()

frutas.remove(frutas[1])
for fruta in frutas:
    print(fruta)

print()