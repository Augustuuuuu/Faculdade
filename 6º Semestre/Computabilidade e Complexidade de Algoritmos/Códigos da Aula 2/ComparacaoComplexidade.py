import time
import os

def comparar_complexidades(n):
    """
    Executa e mede o tempo para algoritmos O(n), O(n^2) e O(n^3)
    para um dado valor de n.
    """
    print(f"\n--- Testando para n = {n} ---")

    # --- Algoritmo O(n) ---
    inicio_on = time.time()
    passos_on = 0
    for i in range(n):
        passos_on += 1
    tempo_on = time.time() - inicio_on
    print(f"O(n):   \t{tempo_on:.6f} segundos ({passos_on} passos)")

    # --- Algoritmo O(n^2) ---
    inicio_on2 = time.time()
    passos_on2 = 0
    for i in range(n):
        for j in range(n):
            passos_on2 += 1
    tempo_on2 = time.time() - inicio_on2
    print(f"O(n²):  \t{tempo_on2:.6f} segundos ({passos_on2} passos)")

    # --- Algoritmo O(n^3) ---
    inicio_on3 = time.time()
    passos_on3 = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                passos_on3 += 1
    tempo_on3 = time.time() - inicio_on3
    print(f"O(n³):  \t{tempo_on3:.6f} segundos ({passos_on3} passos)")


# Limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("="*40)
print("Comparando Complexidades: O(n), O(n²), O(n³)")
print("="*40)

# Lista de valores de 'n' para testar
valores_de_n = [10, 100, 500] 

for n_teste in valores_de_n:
    comparar_complexidades(n_teste)