#Crie um dicionário com nome e idade. Adicione a profissão, altere a idade e
#remova a profissão. No final, percorra o dicionário mostrando chave e valor.

pessoa = {
    "nome": "Carlos",
    "idade": "30"
}

pessoa["profissão"] = "Químico" #adicionando profissão

print()
for chave, valor in pessoa.items():
    print(chave, ":", valor)
print()

pessoa["idade"] = 31 #alterando a idade

del pessoa["profissão"] #removendo profissão

for chave, valor in pessoa.items():
    print(chave, ":", valor)