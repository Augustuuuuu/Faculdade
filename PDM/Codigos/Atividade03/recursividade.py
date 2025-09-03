import time

def fatorial(n):
    inicio = time.perf_counter()  # marca o tempo inicial
    
    resultado = 1
    passos = 0
    
    for i in range(1, n + 1):
        resultado *= i
        passos += 1
    
    fim = time.perf_counter()  # marca o tempo final
    tempo_execucao = fim - inicio
    
    return resultado, passos, tempo_execucao

# Exemplo:
n = 10
resultado, passos, tempo = fatorial(n)

print(f"{n}! = {resultado}")
print(f"Passos (multiplicações): {passos}")
print(f"Tempo de execução: {tempo:.10f} segundos")
