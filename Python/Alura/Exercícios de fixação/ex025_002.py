nomes = []

for i in range(5):
    nome = str(input(f"Digite o {i+1}º nome da lista: ")).title()
    nomes.append(nome)

invertida = nomes[::-1]

print("Original: ", nomes)
print("Invertida: ", invertida)