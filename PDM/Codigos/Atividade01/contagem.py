linhas = int(input("Quantas linhas? "))
colunas = int(input("Quantas colunas? "))

a, b = 0, 1
contador = 0
for i in range(linhas):
    for j in range(colunas):
        print(f"{a:<5} |", end=" ")
        a, b = b, a + b
        contador += 1
    print()

print(f"\nTotal de números impressos: {contador}")
