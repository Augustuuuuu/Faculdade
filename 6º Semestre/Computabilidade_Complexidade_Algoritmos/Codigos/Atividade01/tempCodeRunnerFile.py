import time
import platform
import psutil

try:
    import cpuinfo
except ImportError:
    cpuinfo = None

def somar_numerosQuadraticos(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i**2
    return soma

def get_processador():

    if cpuinfo:
        info = cpuinfo.get_cpu_info()
        return info.get('brand_raw', 'Não identificado')
    
    proc = platform.processor()
    if not proc:
        proc = platform.uname().processor
    if not proc:
        proc = "Não identificado"
    return proc

def info_sistema():
    print("\n--- ESPECIFICAÇÕES DO SISTEMA ---")
    print(f"Sistema Operacional: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Processador: {get_processador()}")
    print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
    print(f"Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
    print(f"Memória Total: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print("---------------------------------\n")

# Programa principal
qtde_testes = int(input("Quantos testes deseja realizar? "))

info_sistema()

tempos = []

for teste in range(1, qtde_testes + 1):
    n = teste * 100
    inicio = time.perf_counter()
    resultado = somar_numerosQuadraticos(n)
    fim = time.perf_counter()
    tempo = fim - inicio
    tempos.append(tempo)
    print(f"Teste {teste}: Somando até {n} → Resultado: {resultado} | Tempo: {tempo:.6f} segundos")

tempo_total = sum(tempos)
tempo_medio = tempo_total / qtde_testes
print("\n--- RESUMO ---")
print(f"Tempo total: {tempo_total:.6f} segundos")
print(f"Tempo médio por teste: {tempo_medio:.6f} segundos")
print("----------------\n")
