#Trabalhando com espaços e alinhamentos
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres. A exclamação vai pro final após um longo espaço reservado ao nome.
print('Prazer em te conhecer {:>20}!'.format(nome)) #Alinha à direita
print('Prazer em te conhecer {:^20}!'.format(nome))#:Centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Centralizado e cercado por sinais de '='