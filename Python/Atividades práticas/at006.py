n = input('Digite algo: ')
print(n.isnumeric()) #Apesar de ser uma str, é numérico se for um número
print(n.isalpha()) #Diz se o que foi digitado é alfabético, retorna T ou F
print(n.isascii()) #Verifica se todos os caracteres pertencem à tabela ASCII
print(n.isdecimal()) #Retorna T ou F. T se o que foi digitado estiver entre 0 e 9
print(n.isdigit()) #Aceita dígitos (decimais, sobrescritos, circundados etc.), mas não letras
print(n.isidentifier()) #Verifica se a string pode ser um nome de variável Python
print(n.islower()) #Retorna True se todas as letras da string forem minúsculas, e houver pelo menos uma letra
print(n.isprintable()) #Retorna True se todos os caracteres forem imprimíveis
print(n.isspace()) #Só retorna True se todos os caracteres forem espaços/brancos
print(n.istitle()) #Retorna T se cada palavra começar com maíscula, tendo o resto em minúscula
print(n.isupper()) #Retorna True se todas as letras forem maiúsculas
print(n.isalnum()) #Retorna T tanto com letras quanto com números