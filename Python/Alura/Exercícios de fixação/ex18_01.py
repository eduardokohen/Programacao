nomes = []

while True:
    nome = input("Nome (ou 'fim'): ")

    if nome.lower() == "fim":
        break
    nomes.append(nome)

print("Nomes cadastrados:")
for nome in nomes:
    print(f"- {nome}")