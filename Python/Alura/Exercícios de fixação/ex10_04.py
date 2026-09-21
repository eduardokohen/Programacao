frutas = []

for i in range(3):
    fruta = input(f"Digite o nome da {i+1}ª fruta: ")
    frutas.append(fruta)

for fruta in frutas:
    print(fruta)
print()

frutas.append("uva")

for fruta in frutas:
    print(fruta)
print()

frutas.remove("banana")
for fruta in frutas:
    print(fruta)

print()