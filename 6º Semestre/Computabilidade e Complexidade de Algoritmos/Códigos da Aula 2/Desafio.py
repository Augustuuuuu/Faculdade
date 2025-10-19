import time
import os

# Limpa o terminal para uma visualização mais limpa
os.system('cls' if os.name == 'nt' else 'clear')

# --- INSTRUÇÃO 1: Defina n diretamente no código ---
# Você pode alterar este valor para ver como o tempo de execução é afetado
n = 10000

print(f"Iniciando comparação com n = {n}\n" + "="*40)

# --- Algoritmo com complexidade O(n) ---

# INSTRUÇÃO 2: Implemente contadores de passos
passos_on = 0

# INSTRUÇÃO 3: Meça o tempo de execução
inicio_on = time.time()

for i in range(n):
    # Cada iteração do loop é contada como um passo
    passos_on += 1

fim_on = time.time()
tempo_on = fim_on - inicio_on

print(f"Resultados para o algoritmo O(n):")
print(f"  - Passos executados: {passos_on}")
print(f"  - Tempo de execução: {tempo_on:.6f} segundos")
print("-"*40)


# --- Algoritmo com complexidade O(n²) ---

# INSTRUÇÃO 2: Implemente contadores de passos
passos_on2 = 0

# INSTRUÇÃO 3: Meça o tempo de execução
inicio_on2 = time.time()

for i in range(n):
    for j in range(n):
        # Cada iteração do loop INTERNO é contada como um passo
        passos_on2 += 1

fim_on2 = time.time()
tempo_on2 = fim_on2 - inicio_on2

print(f"Resultados para o algoritmo O(n²):")
print(f"  - Passos executados: {passos_on2}")
print(f"  - Tempo de execução: {tempo_on2:.6f} segundos")
print("="*40)
print("\n")


# --- INSTRUÇÃO 4: Compare e analise os resultados ---

print("📊 Análise dos Resultados:\n")
print(f"Para uma entrada n = {n}:")
print(f"O loop O(n) executou exatamente {passos_on} passos, como esperado.")
print(f"O loop O(n²) executou {passos_on2} passos, que é o valor de n ao quadrado ({n} * {n}).\n")

if tempo_on > 0:
    diferenca_tempo = tempo_on2 / tempo_on
    print(f"O algoritmo O(n²) foi aproximadamente {diferenca_tempo:.2f} vezes mais lento que o algoritmo O(n).")
else:
    print("O algoritmo O(n) foi tão rápido que seu tempo de execução foi próximo de zero.")

print("\nIsso demonstra na prática como a complexidade quadrática (O(n²)) escala de forma muito mais lenta que a complexidade linear (O(n)), tornando-se rapidamente ineficiente à medida que 'n' aumenta.")