pessoa = {
    "Nome": "Eduardo",
    "Idade": 31
}

pessoa["Profissão"] = "Engenheiro de Software"

print()
for chave, valor in pessoa.items():
    print(chave, ":", valor)
print()

pessoa["Idade"] = 41
del pessoa["Profissão"]

for chave, valor in pessoa.items():
    print(chave, ":", valor)