nomes = []
contador = 1

while True:
    nome = str(input(f"Digite o {contador}º nome ou fim para sair: ")).title()
    contador += 1
    if nome == "Fim":
        break
    nomes.append(nome)
print("NOMES CADASTRADOS:")
for nome in nomes:
    print("-", nome)