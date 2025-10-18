import random
import time
import matplotlib.pyplot as plt

valores_de_teste = [210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
tempos = []

# Gera lista ordenada com 50 números únicos de 0 a 300
lista = sorted(random.sample(range(0, 501), 50))
print("Lista gerada:", lista, "\n")

def buscar_binario(lista, x):
    esq, dir = 0, len(lista) - 1

    while esq <= dir:
        meio = (esq + dir) // 2
        print(f'Comparando x = {x} com {lista[meio]}')

        if lista[meio] == x:
            return True
        elif lista[meio] < x:
            print(f'{x} é MAIOR que {lista[meio]} -> descartando metade ESQUERDA.\n')
            esq = meio + 1
        else:
            print(f'{x} é MENOR que {lista[meio]} -> descartando metade DIREITA.\n')
            dir = meio - 1
    return False

# Testa cada valor de teste
for x in valores_de_teste:
    inicio = time.perf_counter()
    encontrou = buscar_binario(lista, x)
    fim = time.perf_counter()
    tempos.append(fim - inicio)

    if encontrou:
        print(f'O número {x} ESTÁ na lista ✅\n')
    else:
        print(f'O número {x} NÃO ESTÁ na lista ❌\n')

# Plotando os tempos
plt.plot(valores_de_teste, tempos, marker='o')
plt.xlabel("Número testado")
plt.ylabel("Tempo de busca (s)")
plt.title("Tempo de execução da busca binária")
plt.show()