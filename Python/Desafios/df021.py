#Faça um código em python 3 que imprima um triângulo isóceles feito de asteriscos, centralizado. Ao invés de espaços em branco, coloque #. O triângulo deve ter 7 linhas. Use o laço for
linhas = 7

for i in range(1, linhas + 1):
    # quantidade de "espaços" (substituídos por #)
    hashes = linhas - i
    
    # quantidade de asteriscos
    estrelas = 2 * i - 1
    
    print('#' * hashes + '*' * estrelas + '#' * hashes)