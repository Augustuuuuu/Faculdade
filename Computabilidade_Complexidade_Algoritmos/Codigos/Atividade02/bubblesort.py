import random
import time
import matplotlib.pyplot as plt

valores_de_teste = [210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
tempos = []

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True
        if not houve_troca:
            break
    return lista

# Para cada valor de teste, criamos uma lista de 10 elementos aleatórios incluindo o valor
for x in valores_de_teste:
    lista = random.sample(range(0, 501), 9)  # 9 números aleatórios
    lista.append(x)  # adiciona o valor de teste
    random.shuffle(lista)  # embaralha a lista

    inicio = time.perf_counter()
    bubble_sort(lista)
    fim = time.perf_counter()

    tempos.append(fim - inicio)
    print(f"Lista com o valor {x} ordenada em {tempos[-1]:.6f} segundos")

# plotando o tempo de execução x valor de teste
plt.plot(valores_de_teste, tempos, marker='o')
plt.xlabel("Valor de teste")
plt.ylabel("Tempo de ordenação (s)")
plt.title("Tempo de execução do Bubble Sort com valores de teste")
plt.show()