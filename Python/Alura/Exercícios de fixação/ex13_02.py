pessoa = {
    "Nome": "Carlos",
    "Idade": "30"
}

pessoa["Profissão"] = "Químico"

print()

for chave, valor in pessoa.items():
    print(chave, ":", valor)

print()

pessoa["Idade"] = 31
del pessoa["Profissão"]

for chave, valor in pessoa.items():
    print(chave, ":", valor)