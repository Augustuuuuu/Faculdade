from collections import deque

# Mapa da rede de pontos (nome, tempo em minutos)
matriz = [
    [("Asa Norte", 10), ("Setor Hoteleiro Norte", 20), ("Conjunto Nacional", 30)],
    [("SIG", 25), ("Catedral", 10), ("Museu da Republica", 20)],
    [("Pontão", 30), ("Eixinho Sul", 20), ("Hospital de Base", 15)]
]

# Movimentos possíveis (cima, baixo, esquerda, direita)
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dentro_limite(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def buscar_caminhos(inicio, fim):
    """Retorna todos os caminhos possíveis entre dois pontos, com rota e tempo total"""
    caminhos = []
    fila = deque()
    fila.append((inicio, [inicio], matriz[inicio[0]][inicio[1]][1]))

    while fila:
        (x, y), caminho, tempo = fila.popleft()

        if (x, y) == fim:
            caminhos.append((
                [matriz[i][j][0] for (i, j) in caminho],
                tempo
            ))
            continue

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if dentro_limite(nx, ny) and (nx, ny) not in caminho:
                fila.append(((nx, ny), caminho + [(nx, ny)], tempo + matriz[nx][ny][1]))

    return caminhos

def analisar_caminhos(caminhos):
    caminhos.sort(key=lambda x: x[1])
    menor = caminhos[0]
    maior = caminhos[-1]
    intermediarios = caminhos[1:-1]
    return menor, maior, intermediarios

# ---------------------------
# Exemplo de uso
# ---------------------------
inicio = (0, 0)  # Asa Norte
fim = (2, 2)     # Hospital de Base

caminhos = buscar_caminhos(inicio, fim)

print("🚚 Todos os caminhos possíveis:\n")
for rota, tempo in caminhos:
    print(f"   ➝ {' -> '.join(rota)} | Tempo total: {tempo} min")

menor, maior, intermediarios = analisar_caminhos(caminhos)

print("\n📌 Resumo da análise:")
print(f"   ✅ Mais curto: {' -> '.join(menor[0])} | {menor[1]} min")
print(f"   ❌ Mais longo: {' -> '.join(maior[0])} | {maior[1]} min")

if intermediarios:
    print("   ➖ Intermediários:")
    for rota, tempo in intermediarios:
        print(f"      {' -> '.join(rota)} | {tempo} min")
