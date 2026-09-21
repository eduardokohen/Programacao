frutas = []

for i in range (3):
    fruta = str(input(f"Digite o nome da {i+1}ª fruta: ")).lower()
    frutas.append(fruta)

print()
for fruta in frutas:
    print(fruta)
print()

frutas.remove(frutas[1])
frutas.append("uva")

for fruta in frutas:
    print(fruta)