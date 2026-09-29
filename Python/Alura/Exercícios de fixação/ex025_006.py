nomes = []

for i in range(5):
    nome = str(input(f"Digite o {i+1}º nome: ")).title()
    nomes.append(nome)

invertida = nomes[::-1]

print("Lista original: ", nomes)
print("Lista invertida: ", invertida)