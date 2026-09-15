#Crie um programa que receba o nome de uma pessoa, sua idade e
#sua altura. Depois mostre os dados e calcula a idade da pessoa
#daqui há 10 anos.

nome = str(input("Nome: "))
idade = int(input("Idade: "))
altura = float(input("Altura: "))
futuro = idade + 10

print(f"Nome: {nome}.")
print(f"Idade: {idade}.")
print(f"Altura: {altura}.")

if futuro <= 13:
    condicao = "criança"
elif futuro <= 18:
    condicao = "adolescente"
elif futuro <= 30:
    condicao = "jovem"
elif futuro <= 60:
    condicao = "adulto"
else:
    condicao = "idoso"

print(f"A sua idade daqui há 10 anos será de {futuro} anos.")
print(f"Daqui há 10 anos você será um {condicao}.")

