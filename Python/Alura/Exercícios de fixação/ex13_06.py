pessoa = {
    "Nome": "Eduardo",
    "Idade": 40
}

pessoa["Profissão"] = "Engenheiro de Software"

print()
for chave, valor in pessoa.items():
    print(chave, ":", valor)

print()

del pessoa["Profissão"]
pessoa["Idade"] = 41

for chave, valor in pessoa.items():
    print(chave, ":", valor)