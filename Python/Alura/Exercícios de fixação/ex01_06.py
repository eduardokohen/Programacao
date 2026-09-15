from datetime import date

nome = str(input("Informe o nome: "))
ano_nascimento = int(input("Informe o ano de nascimento: "))
altura = float(input("Informe a altura: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
futuro = idade + 10

if futuro <= 12:
    condicao = "criança"
elif futuro <= 18:
    condicao = "adolescente"
elif futuro <= 25:
    condicao = "jovem"
elif futuro <= 60:
    condicao = "adulto(a)"
else:
    condicao = "idoso(a)"

print(f"Nome: {nome}.")
print(f"Idade: {idade} anos.")
print(f"Altura: {altura}")
print(f"Idade em 10 anos: {futuro}")
print(f"Daqui há 10 anos {nome} será um(a) {condicao}.")