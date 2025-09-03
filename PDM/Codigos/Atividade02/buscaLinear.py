import random
import time
import matplotlib.pyplot as plt

valores_de_teste = [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
tempos = []

for v in valores_de_teste:
    num_array = list(range(v + 1))  # vetor de 0 até v

    inicio = time.perf_counter()
    random_array = random.sample(num_array, v)  # sorteia v números únicos
    fim = time.perf_counter()

    tempos.append(fim - inicio)

# gerar gráfico
plt.plot(valores_de_teste, tempos, marker="o")
plt.xlabel("Tamanho do vetor (N)")
plt.ylabel("Tempo de resposta (segundos)")
plt.title("Tempo de execução da busca linear com diferentes N")
plt.grid(True)
plt.show()