import time

def fibonacci_recursiva_lista(n):
    """Retorna a lista de Fibonacci até o n-ésimo termo usando recursão."""
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    lista = fibonacci_recursiva_lista(n - 1)  # chama recursivamente até n-1
    lista.append(lista[-1] + lista[-2])      # adiciona o n-ésimo termo
    return lista

def proporcao_aurea_fibonacci_recursiva(n):
    inicio = time.perf_counter()
    
    fib = fibonacci_recursiva_lista(n)
    phi_aprox = fib[-1] / fib[-2]
    
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    
    return phi_aprox, tempo_execucao, fib

# Exemplo: 20 passos (mais rápido do que 40 para recursão)
phi, tempo, sequencia = proporcao_aurea_fibonacci_recursiva(20)

print(f"Aproximação da proporção áurea: {phi}")
print(f"Tempo de execução: {tempo:.6f} segundos")
print(f"Quantidade de passos: {len(sequencia) - 1}")
print(f"Sequência de Fibonacci: {sequencia}")
