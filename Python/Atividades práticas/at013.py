nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer {}!' .format(nome)) #Imprime o nome
print('Prazer em te conhecer {:20}!' .format(nome)) #Imprime o nome em 20 caracteres
print('Prazer em te conhecer {:>20}!' .format(nome)) #Imprime o nome em 20 caracteres com alinhamento à direita
print('Prazer em te conhecer {:^20}!' .format(nome)) #Imprime o nome em 20 caracteres com alinhamento centralizado
print('Prazer em te conhecer {:=^20}!' .format(nome)) #Imprime em 20 caracteres centralizado com sinais de = em torno