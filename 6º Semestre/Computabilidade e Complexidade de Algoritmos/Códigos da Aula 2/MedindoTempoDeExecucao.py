import os, time
os.system('cls' if os.name == 'nt' else 'clear')
n = 100000
inicio = time.time()
soma = 0
for i in range(n):
    soma += i
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} s")
print(f"Soma total = {soma}")