n = 5
soma = 0

for i in range(n + 1):
    soma += i ** 2
    print(f"Passo {i+1} - {soma}")

print(f"Soma total = {soma}")