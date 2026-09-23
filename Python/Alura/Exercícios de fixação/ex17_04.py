print("="*60)
print("FIBONACCI".center(60))
print("="*60)

n = int(input("Informe a quantidade de termos: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end = " ")

    novo_a = b
    novo_b = a + b
    i += 1

    a = novo_a
    b = novo_b
print()
print("="*60)