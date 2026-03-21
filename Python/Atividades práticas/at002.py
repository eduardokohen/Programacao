#Nesse bloco de código vemos um valor numérico como uma string, o padrão caso não seja declarado
#o tipo primitivo
n1=input('Digite um valor: ')
print(type(n1))

#Nesse bloco de código declaramos que o tipo primitivo deve ser um número inteiro
#Agora sim o tipo aparecerá como int
n2=int(input('Digite um valor: '))
print(type(n2))

#Aqui vamos definir o tipo primitivo como um float
n3=float(input('Digite um valor: '))
print(type(n3))