nomes = []

for i in range(5):
    nome = str(input(f"Digite o {i+1}º nome: ")).title()
    nomes.append(nome)

invertida = nomes[::-1]

print(f"Lista original: {nomes}")
print(f"Lista invertida: {invertida}")