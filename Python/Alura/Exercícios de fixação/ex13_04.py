pessoa = {
    "Nome": "Carlos",
    "Idade": "30"
}

pessoa["Profissão"] = "Químico"

print()
for chave, valor in pessoa.items():
    print(chave, ":", valor)
print()

del pessoa["Profissão"]
pessoa["Idade"] = 31

for chave, valor in pessoa.items():
    print(chave, ":", valor)