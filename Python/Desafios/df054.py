#Desenlvolva um programa que peça três retas ao usuário e diga se elas formam um triângulo

retas = []

for i in range(3):
    valor = int(input(f'Digite a medida da {i+1}ª reta: '))
    retas.append(valor)

if (retas[0] + retas[1] > retas[2] and
    retas[0] + retas[2] > retas[1] and
    retas[1] + retas[2] > retas[0]):
    print(f'As retas {retas[0]}, {retas[1]} e {retas[2]} formam um triângulo')
else:
    print(f'As retas {retas[0]}, {retas[1]} e {retas[2]} não formam um triângulo')