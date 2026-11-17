
pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite sua cidade: ")
}

texto = f"""Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Cidade: {pessoa['cidade']}
"""

print(texto)