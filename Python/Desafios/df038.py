n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunnda nota: '))
n3 = float(input('Digite a terceira nota: '))

m = (n1+n2+n3)/3

if m == 10:
    print(f'Excelente! Gabaritou com {m:.1f}.')
elif 10 > m >= 6:
    print(f'Aluno aprovado com média {m:.1f}.')
elif 5 <= m < 6:
    print(f'Aluno apto para o exame de recuperação com média {m:.1f}.')
elif 5 > m >= 1:
    print(f'Aluno reprovado com média {m:.1f}.')
else:
    print(f'Aluno burro pra caralho. Média de {m:.1f}')