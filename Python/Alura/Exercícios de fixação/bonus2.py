from datetime import date

nome = str(input("Informe seu nome: ")).title()
ano_nascimento = int(input("Informe o ano de seu nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

texto = f"""
Muito prazer, {nome}. 
Vejo que você tem {idade} anos.
"""

print(texto)