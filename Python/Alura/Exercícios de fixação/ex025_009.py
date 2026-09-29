nomes = []
invertida = []

for i in range(5):
    nome = str(input(f"Digite o {i+1}º nome: ")).title()
    nomes.append(nome)

for nome in nomes:
    invertida.insert(0, nome)

print("Lista original: ", nomes)
print("Lista invertida: ", invertida)