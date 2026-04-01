nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    condicao = 'reprovado'
elif 5 <= media <= 6.99:
    condicao = 'de recuperação'
else:
    condicao = 'aprovado'
     
print('Você está {}'.format(condicao))