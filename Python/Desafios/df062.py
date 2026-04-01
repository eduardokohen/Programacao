#Faça um programa que leia a idade de um nadador e o classifique.
#Até 19 anos: mirim, até 14 anos: infantil, até 19 anos: júnior,
#Até 20 anos: sênior e acima de 20 anos: master

idade = int(input('Informe a sua idade: '))

if idade <= 9:
    categoria = 'mirim'
elif 9 < idade <= 14:
    categoria = 'infantil'
elif 14 < idade <= 19:
    categoria = 'júnior'
elif 19 < idade <= 20:
    categoria = 'sênior'
else:
    categoria = 'master'
    
print('Você está na categoria {}.'.format(categoria))