from datetime import date

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Informe o ano do seu nascimento: "))
altura = float(input("Qual é a sua altura? "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
futuro = idade + 10

if futuro <= 12:
    condicao = "infante"
elif futuro <= 18:
    condicao = "adolescente"
elif futuro <= 25:
    condicao = "jovem"
elif futuro <= 60:
    condicao = "adulto"
else:
    condicao = "idoso"

print(f"Nome: {nome.title()}.")
print(f"Idade: {idade}.")
print(f"Altura: {altura}.")
print(f"Idade em 10 anos: {futuro}")
print(f"Daqui há 10 anos você será um {condicao}.")