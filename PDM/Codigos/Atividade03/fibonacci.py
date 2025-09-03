def fibonacci(n):
    a, b = 0, 1
    sequencia = []
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia
if __name__ == "__main__":
    print(fibonacci(30))