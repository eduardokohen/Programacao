from datetime import date
ano_atual = date.today().year

nome = str(input("Digite o nome do atleta: "))
ano_nascimento = int(input("Informe o ano do seu nascimento: "))

idade = ano_atual - ano_nascimento

if idade <= 9:
    situacao = "mirim"
elif idade <= 14:
    situacao = "infantil"
elif idade <= 19:
    situacao = "júnior"
elif idade <= 25:
    situacao = "sênior"
else:
    situacao = "master"

texto = f"""O atleta {nome} tem {idade} anos.
Ele está na categoria {situacao}."""

print(texto)