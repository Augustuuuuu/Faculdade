import time

# contador de passos (global)
passos = 0

def fibonacci(n):
    global passos
    passos += 1  # conta cada chamada da função
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

quantidade = 30

inicio = time.perf_counter()
for i in range(quantidade):
    print(fibonacci(i), end=" ")
fim = time.perf_counter()

print(f"\nTempo de execução total: {fim - inicio:.10f} segundos")
print(f"Número de passos (chamadas de função): {passos}")
