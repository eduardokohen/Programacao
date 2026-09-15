#Criando a lista de frutas:

frutas = []

for i in range(3):
    fruta = str(input(f"Digite a {i+1}ª fruta: "))
    frutas.append(fruta)

#Acessando ítens da lista

frutas.append("uva") #Adicionando itens à lista
escolha = int(input("Qual fruta você gostaria de acessar? "))
print(f"A fruta que você acessou é: {frutas[escolha - 1]}.")
print(frutas[0:4])
frutas[0] = "graviola" #alterando itens da lista
print(frutas)

#removendo itens da lista
frutas.remove("uva")
frutas.pop() #Removendo o último item da lista
print(frutas)

#Percorrendo um lista:

for fruta in frutas:
    print(fruta)