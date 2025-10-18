import os
os.system('cls' if os.name == 'nt' else 'clear')
n = 5
def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma
print(somatorio(n))