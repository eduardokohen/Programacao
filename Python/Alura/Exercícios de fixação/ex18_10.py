nomes = []
i = 1

while True:
    nome = str(input(f"Digite o {i}º nome ou fim para sair: ")).title()
    i+= 1
    
    if nome == "Fim":
        break
    nomes.append(nome)

print("NOMES CADASTRADOS:")

for nome in nomes:
    print("-", nome)