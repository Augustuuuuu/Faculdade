import os, time
os.system("cls" if os.name == "nt" else "clear")
n = 1000
inicio = time.time()
soma = 0
for i in range(n+1):
    soma += 1
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.10f}s")
print(f"Soma total = {soma}")
