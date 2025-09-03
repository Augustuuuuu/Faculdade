def proporcao_aurea_fibonacci(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib [-2])

    aurea = fib[-1] / fib[-2]
    return aurea, fib
if __name__ == "__main__":
    aurea, sequencia = proporcao_aurea_fibonacci(30)
    print(f"Sequência de Fibonacci até o 30º termo: {sequencia}\n")
    print(f"Aproximação de proporção áurea: {aurea}")
