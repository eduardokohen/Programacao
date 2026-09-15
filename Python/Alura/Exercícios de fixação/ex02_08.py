notas = []

nome = str(input("Informe o nome do aluno: ")).title()

for i in range (1, 11, 1):
    nota = float(input(f"Informe a {i}ª nota: "))
    notas.append(nota)

    inserir = str(input(f"Deseja inserir uma {i+1}ª nota? (s/n) ")).lower()
    if inserir == "n":
        break

media = sum(notas)/len(notas)

if media < 5:
    condicao = "reprovado(a)"
elif media < 7: 
    condicao = "de recuperação"
elif media <= 8:
    condicao = "aprovado(a)"
else:
    condicao = "aprovado(a) com louvor"

print(f"As notas de {nome} são: {notas}.")
print(f"A media das notas é: {media:.2f}.")
print(f"{nome} está {condicao}")