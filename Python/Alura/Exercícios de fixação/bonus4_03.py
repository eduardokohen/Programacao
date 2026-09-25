notas = []
nome = str(input("Digite o nome do aluno: ")).title()

for i in range(5):
    
    while True:

        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
        else:
            notas.append(nota)
            break

menor = notas[0]
maior = notas[0]

for nota in notas:
    if nota < menor:
        menor = nota
    if nota > maior:
        maior = nota

media = sum(notas)/len(notas)

texto = f"""
As notas de {nome} são: {notas}.
A maior nota é: {maior}.
A menor nota é: {menor}.
A média das notas é: {media:.2f}.
"""

print(texto)