frase = input('Digite uma frase: ')

print(frase.strip()) #Útil para remover espaços antes e após a string
print(len(frase.strip())) #Calcula a quantidade de caracteres que existem na string, sem espaços
print(frase.rstrip()) #Remove apenas os espaços no final da string
print(frase.lstrip()) #Remove apenas os espaços no início da string
print('-'.join(frase.split())) #junta todos elementos da frase usando um '-' como separador

nova_lista = frase.split()

print(nova_lista[0]) #imprime a palavra na posição 0.
print(nova_lista) #imprime a frase após a aplicação do split
print(frase.upper().count('O'))

for letra in nova_lista: #Mostra todas as letras na posição 0
    print(letra[0])