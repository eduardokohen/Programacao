from datetime import date

ano_atual = date.today().year

nome = str(input("Informe o nome do(a) atleta: "))
nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - nascimento

if idade <= 9:
    categoria = 'mirim'
elif idade <= 14:
    categoria = 'infantil'
elif idade <= 19:
    categoria = 'júnior'
elif idade <= 25:
    categoria = 'sênior'
else:
    categoria = 'master'

texto = f"""O(A) atleta {nome} tem {idade} anos.
Está na categoria {categoria}."""

print(texto)