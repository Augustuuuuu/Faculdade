# Recursividade 
# Cada boneca contém outra menor -> quando chega à menor, para (caso base).
# Montar sequência de volta = combinar soluções menores.
import os
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    resultado = fatorial(5)
    print(f"Resultado: {resultado}")