nomes = []
idades = []

for i in range(3):
    nome = str(input(f"Digite o nome do {i+1}º membro da lista: ")).title()
    nomes.append(nome)

for i in range(3):
    idade = int(input(f"Digite a idade do {i+1}º membro da lista: "))
    idades.append(idade)

pessoas = {}

for i in range(3):
    pessoas[nomes[i]] = idades[i]

print(pessoas)