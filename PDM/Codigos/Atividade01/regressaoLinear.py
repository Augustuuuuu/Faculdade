import os, time
os.system("cls" if os.name == "nt" else "clear")
i = 1000
n = i
inicio = time.time()
contador_passos = 0
while i > 1:
    print(f"Passo {contador_passos}: i = {i}")
    i = i // 2
    contador_passos += 1
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.10f}s")
print(f"\nPassos finalizados")
print(f"Para reduzir n = {n} até 1, foram necessário {contador_passos} passos.")
