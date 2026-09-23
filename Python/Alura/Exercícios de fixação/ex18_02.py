nomes = []

while True:
    nome = str(input("Digite um nome ou fim para sair: ")).title()

    if nome.lower() == "fim":
        break
    nomes.append(nome)

print("NOMES CADASTRADOS:")
for nome in nomes:
    print("-", nome)