nomes = []
idades = []

for i in range (3):
    nome = str(input(f"Digite o {i+1}º nome: ")).title()
    nomes.append(nome)

for j in range (3):
    idade = int(input(f"Digite a idade do {i+1}º membro da lista: "))
    idades.append(idade)

pessoas = {nome:idade for nome, idade in zip(nomes,idades)}
print(pessoas)