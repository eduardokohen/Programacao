pessoa = {}

pessoa["nome"] = input("Digite o nome: ")
pessoa["idade"] = int(input("Digite a idade: "))

#Acessar o valor da chave nome:
print(pessoa)
print(pessoa["nome"])

#acesso com get:
print(pessoa.get("telefone", "valor não informado"))

pessoa["cidade"] = input("Digite a cidade: ")
print(pessoa)

#Atualizar o valor de idade:
print(pessoa["idade"])
pessoa["idade"] = pessoa["idade"] + 1
print(pessoa["idade"])

#usando laço para iterar e imprimir valor:
for chave, valor in pessoa.items():
    print(chave, "->", valor)

#removendo o último valor com o pop:

pessoa.pop("cidade")
print(pessoa)