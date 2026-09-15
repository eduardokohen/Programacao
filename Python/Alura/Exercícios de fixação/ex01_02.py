from datetime import date

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Informe o ano do seu nascimento: "))
altura = float(input("Qual é a sua altura? "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
futuro = idade + 10

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Idade daqui há 10 anos: {futuro}")

if idade <= 12:
    condicao = "infante"
elif idade <= 18:
    condicao = "adolescente"
elif idade <= 25:
    condicao = "jovem"
elif idade <= 60:
    condicao = "adulto"
else:
    condicao = "idoso"

print(f"Daqui há 10 anos você será um {condicao}.")