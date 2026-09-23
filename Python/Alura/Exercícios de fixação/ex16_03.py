print("="*60)
print("FIBONACCI".center(60))
print("="*60)

n = int(input("Informe a quantidade de termos: "))

a = 0
b=1

for i in range(n):
    print(a, end = " ")

    novo_a = b
    novo_b = a + b

    a = novo_a
    b = novo_b

print()