import os

def analise_reducao_nao_linear(n):
    """
    Conta quantos passos um loop leva para terminar quando a variável
    de controle é dividida por 2 a cada iteração.
    """
    passos = 0
    i = n
    while i > 0:
        # A operação principal do loop
        i = i // 2  # Divisão inteira
        passos += 1
    
    print(f"Para n = {n}, o loop executou {passos} vezes.")


# Limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("="*50)
print("Analisando Loop com Redução Não Linear (i = i // 2)")
print("="*50)

analise_reducao_nao_linear(10)
analise_reducao_nao_linear(100)
analise_reducao_nao_linear(1000)
analise_reducao_nao_linear(100000)
analise_reducao_nao_linear(1000000)