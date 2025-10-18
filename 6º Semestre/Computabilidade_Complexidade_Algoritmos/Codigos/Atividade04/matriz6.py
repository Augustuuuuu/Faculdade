# -*- coding: utf-8 -*-
"""
Solução completa e INTERATIVA para os exercícios da Aula 6 de Computabilidade.

Este script contém:
1. Uma solução INTERATIVA para o "Desafio 6x6: Rede Metropolitana" com visualização gráfica.
2. A solução para o "Desafio de Alocação 6x6".
3. Funções para gerar os gráficos de análise de performance.

Requisitos:
- numpy
- scipy
- matplotlib

Instale as dependências com: pip install numpy scipy matplotlib
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import heapq  # Importado para usar a fila de prioridade (heap) no algoritmo de Dijkstra

try:
    from scipy.optimize import linear_sum_assignment
except ImportError:
    linear_sum_assignment = None

# --- DADOS GLOBAIS PARA O EXERCÍCIO 1 ---
COSTS_EX1 = np.array([
    [20, 45, 35, 40, 30, 32], [ 3, 22, 28, 31, 30, 26],
    [24, 20, 38, 30, 33, 29], [35, 37, 31, 27, 25, 32],
    [45, 60, 40, 36, 33, 42], [40, 50, 43, 39, 48, 25]
])

LOCATIONS_EX1 = np.array([
    ["SIG", "Esplanada", "Rodoviária", "Torre de TV", "Setor Hoteleiro Norte", "Conjunto Nacional"],
    ["Sudoeste", "Setor Bancário", "Catedral", "Museu da República", "Setor Cultural", "Biblioteca Nacional"],
    ["Eixinho Sul", "Parque da Cidade", "Mané Garrincha", "Funarte", "Setor Comercial Sul", "Galeria dos Estados"],
    ["Asa Norte", "Setor Militar", "Setor Hoteleiro Sul", "Autarquias", "Estação Central", "Teatro Nacional"],
    ["Pontão", "Ponte JK", "ParkShopping", "EPTG", "Guará", "Águas Claras"],
    ["SCES", "Ermida", "QI 11", "Parkway", "Taguatinga", "Aeroporto BSB"]
])

# --- Exercício 1: Rede Metropolitana (Versão Interativa) ---

def print_locations_menu(locations):
    """Exibe o menu de localizações para o usuário escolher."""
    print("\n--- Menu de Localizações ---")
    num = 1
    for row in locations:
        for loc in row:
            print(f"{num:2d}. {loc:<25}", end="")
            if num % 3 == 0:
                print()
            num += 1
    print("\n" + "-"*28)

def get_user_choice(prompt, max_choice):
    """Obtém e valida a escolha numérica do usuário, tratando a opção de sair."""
    while True:
        try:
            choice = int(input(prompt))
            if choice == 0:
                return -1 # Sinaliza a saída
            if 1 <= choice <= max_choice:
                return choice - 1 # Retorna o índice (base 0)
            else:
                print(f"Erro: Por favor, insira um número entre 1 e {max_choice} (ou 0 para sair).")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número.")

def visualize_route(locations, costs, path_coords, start_pos, end_pos):
    """Gera uma visualização gráfica da rota sobre a matriz de custos."""
    rows, cols = costs.shape
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Desenha o heatmap da matriz de custos
    im = ax.imshow(costs, cmap="viridis_r")
    
    # Adiciona a barra de cores
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Custo do Terreno (minutos)", rotation=-90, va="bottom")
    
    # Adiciona os nomes e custos nas células
    for i in range(rows):
        for j in range(cols):
            text_color = "black" if costs[i, j] < 45 else "white"
            ax.text(j, i, f"{locations[i, j]}\n({costs[i, j]})",
                    ha="center", va="center", color=text_color, fontsize=8)
                    
    # Desenha a rota ótima
    if path_coords:
        path_rows, path_cols = zip(*path_coords)
        ax.plot(path_cols, path_rows, color='red', linestyle='-', linewidth=3, marker='o', markersize=8, label='Rota Ótima')
        
        # Destaca início e fim
        ax.plot(start_pos[1], start_pos[0], 'go', markersize=15, label='Origem')
        ax.plot(end_pos[1], end_pos[0], 'yo', markersize=15, label='Destino')

    ax.set_title("Visualização Gráfica da Rota Ótima")
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.legend()
    
    fig.tight_layout()
    plt.show()


def find_optimal_path_dijkstra(start_pos, end_pos, costs, locations):
    """Calcula o caminho ótimo entre quaisquer dois pontos usando o algoritmo de Dijkstra."""
    rows, cols = costs.shape
    distances = np.full((rows, cols), np.inf)
    previous_nodes = {}
    pq = [(costs[start_pos], start_pos)]
    distances[start_pos] = costs[start_pos]

    while pq:
        current_cost, current_pos = heapq.heappop(pq)
        if current_cost > distances[current_pos]:
            continue
        if current_pos == end_pos:
            break
        current_row, current_col = current_pos
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                neighbor_row, neighbor_col = current_row + dr, current_col + dc
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    neighbor_pos = (neighbor_row, neighbor_col)
                    new_cost = current_cost + costs[neighbor_pos]
                    if new_cost < distances[neighbor_pos]:
                        distances[neighbor_pos] = new_cost
                        previous_nodes[neighbor_pos] = current_pos
                        heapq.heappush(pq, (new_cost, neighbor_pos))

    final_cost = distances[end_pos]
    if np.isinf(final_cost):
        return "Não foi possível encontrar um caminho.", None, []

    path = []
    step = end_pos
    while step != start_pos:
        path.append(step)
        if step not in previous_nodes:
             return "Não foi possível reconstruir o caminho.", None, []
        step = previous_nodes[step]
    path.append(start_pos)
    path.reverse()
    path_names = [locations[r, c] for r, c in path]
    return ' -> '.join(path_names), final_cost, path

def interactive_metropolitan_solver():
    """Função principal que gerencia a interação com o usuário para o Exercício 1."""
    print("--- Exercício 1: Calculadora de Rota Ótima (Interativa) ---")
    while True:
        print_locations_menu(LOCATIONS_EX1)
        max_locs = LOCATIONS_EX1.size
        start_choice = get_user_choice(f"Escolha o número da ORIGEM (1-{max_locs}, ou 0 para sair): ", max_locs)
        if start_choice == -1:
            break
        end_choice = get_user_choice(f"Escolha o número do DESTINO (1-{max_locs}, ou 0 para sair): ", max_locs)
        if end_choice == -1: # Sai se o usuário digitar 0 para o destino também
            break
        if start_choice == end_choice:
            print("\nAVISO: A origem e o destino não podem ser os mesmos. Tente novamente.\n")
            continue
            
        start_pos = (start_choice // 6, start_choice % 6)
        end_pos = (end_choice // 6, end_choice % 6)
        
        path_str, cost, path_coords = find_optimal_path_dijkstra(start_pos, end_pos, COSTS_EX1, LOCATIONS_EX1)
        
        if cost is not None:
            # Primeiro, mostra a visualização gráfica (que pausa o programa)
            visualize_route(LOCATIONS_EX1, COSTS_EX1, path_coords, start_pos, end_pos)
            
            # Após o usuário fechar o gráfico, mostra o resultado em texto
            print("\n--- Resultado da Rota ---")
            print(f"  Custo Mínimo: {cost:.0f} minutos")
            print(f"  Caminho Ótimo: {path_str}")
        else:
            # Se não houver rota, apenas imprime a mensagem de erro
            print("\n--- Resultado da Rota ---")
            print(f"  {path_str}")
        
        print("-" * 25 + "\n")
        
        # Pergunta ao usuário se deseja continuar
        while True:
            another = input("Deseja calcular uma nova rota? (s/n): ").lower()
            if another in ['s', 'sim', 'n', 'nao', 'não']:
                break
            else:
                print("Opção inválida. Por favor, digite 's' ou 'n'.")
        
        if another in ['n', 'nao', 'não']:
            break # Encerra a parte interativa

# --- Exercício 2: Desafio de Alocação 6x6 ---

def solve_allocation_challenge():
    """Resolve o Desafio de Alocação 6x6 e compara a solução ótima com a gananciosa."""
    if linear_sum_assignment is None:
        print("\n--- Exercício 2: Desafio de Alocação 6x6 ---")
        print("Não foi possível executar: biblioteca SciPy não encontrada.")
        return

    print("\n--- Exercício 2: Desafio de Alocação 6x6 ---")
    costs = np.array([
        [31, 52, 46, 44, 49, 36], [34, 33, 41, 37, 45, 39],
        [29, 47, 38, 35, 43, 40], [40, 36, 42, 34, 38, 35],
        [33, 39, 37, 36, 34, 41], [35, 38, 40, 33, 36, 32]
    ])
    motoristas = ["A", "B", "C", "D", "E", "F"]
    regioes = ["R1 Asa N.", "R2 Lago S.", "R3 Taguating.", "R4 Guará", "R5 Á Claras", "R6 Aerop."]

    # Solução Ótima (Algoritmo Húngaro)
    row_ind, col_ind = linear_sum_assignment(costs)
    optimal_cost = costs[row_ind, col_ind].sum()
    print("\nSolução Ótima (Algoritmo Húngaro/PD):")
    assignments = sorted(zip(row_ind, col_ind))
    for motorista_idx, regiao_idx in assignments:
        cost = costs[motorista_idx, regiao_idx]
        print(f"  Motorista {motoristas[motorista_idx]} -> {regioes[regiao_idx]} (Custo: {cost} min)")
    print(f"  -> Tempo Mínimo Total: {optimal_cost} minutos")

    # Solução Gananciosa (por Motorista)
    greedy_cost = 0
    remaining_regions = list(range(costs.shape[1]))
    print("\nSolução Gananciosa (por Motorista):")
    for i in range(len(motoristas)):
        best_cost_for_driver = np.inf
        best_region_idx = -1
        for region_idx in remaining_regions:
            if costs[i, region_idx] < best_cost_for_driver:
                best_cost_for_driver = costs[i, region_idx]
                best_region_idx = region_idx
        greedy_cost += best_cost_for_driver
        remaining_regions.remove(best_region_idx)
        print(f"  Motorista {motoristas[i]} -> {regioes[best_region_idx]} (Custo: {best_cost_for_driver} min)")
    print(f"  -> Tempo Total (Ganancioso): {greedy_cost} minutos")

    print("\nComparação de Performance Quantitativa:")
    print(f"  Ótimo (PD):   {optimal_cost} minutos")
    print(f"  Ganancioso: {greedy_cost} minutos")
    print(f"  Diferença:  {greedy_cost - optimal_cost} minutos")

# --- Geração de Gráficos de Performance ---

def generate_performance_graphs():
    """Gera gráficos que comparam a complexidade de diferentes abordagens."""
    print("\n--- Gráficos de Análise de Performance ---")

    # Gráfico 1: Caminho na Grade
    plt.figure(figsize=(10, 6))
    N_grid = np.arange(1, 15)
    # Evita log(0)
    safe_log_arg = (N_grid**2).astype(float)
    safe_log_arg[safe_log_arg == 0] = 1
    dijkstra_ops = N_grid**2 * np.log(safe_log_arg)
    brute_force_ops_grid = [3**(n+n) for n in N_grid]
    plt.plot(N_grid, dijkstra_ops, 'g-o', label='Dijkstra (O(N² log N))')
    plt.plot(N_grid, brute_force_ops_grid, 'r-o', label='Força Bruta (O(3²ᴺ))')
    plt.yscale('log')
    plt.title('Performance: Dijkstra vs. Força Bruta para Caminho na Grade')
    plt.xlabel('Tamanho da Grade (N x N)')
    plt.ylabel('Número de Operações (Escala Logarítmica)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("performance_grade.png")
    print("Gráfico 'performance_grade.png' salvo.")

    # Gráfico 2: Alocação
    plt.figure(figsize=(10, 6))
    N_alloc = np.arange(1, 15)
    hungarian_ops = N_alloc**3
    brute_force_ops_alloc = [math.factorial(n) for n in N_alloc]
    plt.plot(N_alloc, hungarian_ops, 'b-o', label='Algoritmo Húngaro (O(N³))')
    plt.plot(N_alloc, brute_force_ops_alloc, 'r-o', label='Força Bruta (O(N!))')
    plt.yscale('log')
    plt.title('Performance: Algoritmo Húngaro vs. Força Bruta para Alocação')
    plt.xlabel('Número de Motoristas/Tarefas (N)')
    plt.ylabel('Número de Operações (Escala Logarítmica)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("performance_alocacao.png")
    print("Gráfico 'performance_alocacao.png' salvo.")
    
    # Exibe os gráficos no final da execução
    plt.show()


if __name__ == '__main__':
    interactive_metropolitan_solver()
    
    # Executa as outras partes do script após sair do modo interativo.
    solve_allocation_challenge()
    generate_performance_graphs()
    
    print("\nPrograma finalizado.")

