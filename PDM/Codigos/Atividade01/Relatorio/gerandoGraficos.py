import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==============================================================================
# === Dados (Os dados originais foram mantidos sem alterações) ===
# ==============================================================================

# Máquina 1
dados_m1_linear = {
    "INPUT": [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000],
    "TEMPO": [0.000917,0.001663,0.002141,0.002734,0.003383,0.004199,0.005192,0.004676,0.005421,0.007558,0.007597,0.007016,0.006619,0.012087,0.020440,0.014114,0.011889,0.011936,0.013241,0.013964]
}
dados_m1_quad = {
    "INPUT": [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000],
    "TEMPO": [0.000830,0.001516,0.002338,0.003098,0.004814,0.006026,0.006224,0.008935,0.010389,0.020465,0.025304,0.019437,0.021871,0.027107,0.030383,0.021983,0.022216,0.030577,0.032936,0.027793]
}
dados_m1_log = {
    "INPUT": [1e50,1e53,6e54,1e56,1e57,6e57,3e58,1e59,3e59,1e60,3e60,6e60,1e61,3e61,6e61,1e62,2e62,4e62,6e62,1e63],
    "TEMPO": [0.000030,0.000045,0.000027,0.000034,0.000035,0.000032,0.000032,0.000032,0.000031,0.000034,0.000035,0.000034,0.000031,0.000031,0.000032,0.000034,0.000033,0.000035,0.000035,0.000036]
}

# Máquina 2
dados_m2_linear = {
    "INPUT": [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000],
    "TEMPO": [0.000233,0.000439,0.000631,0.000992,0.001083,0.001300,0.001850,0.002698,0.002469,0.002176,0.002523,0.003257,0.003206,0.004266,0.003949,0.004238,0.004684,0.004438,0.005668,0.005483]
}
dados_m2_quad = {
    "INPUT": [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000],
    "TEMPO": [0.000434,0.001061,0.001661,0.001830,0.002450,0.003083,0.003607,0.003643,0.004363,0.004887,0.005063,0.005660,0.006028,0.006706,0.007347,0.007662,0.008502,0.009317,0.008661,0.009746]
}
dados_m2_log = {
    "INPUT": [1e50,1e53,6e54,1e56,1e57,6e57,3e58,1e59,3e59,1e60,3e60,6e60,1e61,3e61,6e61,1e62,2e62,4e62,6e62,1e63],
    "TEMPO": [0.000023,0.000067,0.000023,0.000023,0.000022,0.000025,0.000024,0.000041,0.000045,0.000026,0.000027,0.000029,0.000059,0.000027,0.000048,0.000025,0.000027,0.000016,0.000028,0.000025]
}

# ==============================================================================
# === Funções de Plotagem Corrigidas ===
# ==============================================================================

# Função para plotar os gráficos com escala LINEAR (para O(n) e O(n²))
def plot_comparacao_linear(dados1, dados2, titulo, nome_arquivo):
    df1 = pd.DataFrame(dados1)
    df2 = pd.DataFrame(dados2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df1["INPUT"], df1["TEMPO"], marker="o", linestyle="-", label="Máquina 1")
    plt.plot(df2["INPUT"], df2["TEMPO"], marker="o", linestyle="-", label="Máquina 2")
    
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo de execução (s)")
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    # Formata os números do eixo X para notação normal, não científica, melhorando a leitura
    plt.ticklabel_format(style='plain', axis='x') 
    plt.savefig(nome_arquivo)
    plt.close()

# Função para plotar o gráfico com escala LOGARÍTMICA no eixo X (para O(log n))
def plot_comparacao_log(dados1, dados2, titulo, nome_arquivo):
    df1 = pd.DataFrame(dados1)
    df2 = pd.DataFrame(dados2)
    
    plt.figure(figsize=(10, 6))
    
    # === ALTERAÇÃO PRINCIPAL ===
    # A linha abaixo define a escala do eixo X como logarítmica.
    # Essencial para visualizar entradas que crescem exponencialmente.
    plt.xscale('log')
    
    plt.plot(df1["INPUT"], df1["TEMPO"], marker="o", linestyle="-", label="Máquina 1")
    plt.plot(df2["INPUT"], df2["TEMPO"], marker="o", linestyle="-", label="Máquina 2")
    
    plt.xlabel("Tamanho da entrada (n) - Escala Logarítmica")
    plt.ylabel("Tempo de execução (s)")
    plt.title(titulo)
    plt.legend()
    # "which='both'" ativa as linhas de grade primárias e secundárias, útil em escalas log
    plt.grid(True, which="both", ls="-")
    plt.savefig(nome_arquivo)
    plt.close()

# ==============================================================================
# === Geração dos Gráficos ===
# ==============================================================================

# Gerar gráficos individuais com a função de plotagem correta para cada caso
print("Gerando gráfico linear...")
plot_comparacao_linear(dados_m1_linear, dados_m2_linear, "Comparação de Desempenho - Soma Linear (O(n))", "grafico_linear.png")

print("Gerando gráfico quadrático...")
plot_comparacao_linear(dados_m1_quad, dados_m2_quad, "Comparação de Desempenho - Soma Quadrática (O(n²))", "grafico_quadratico.png")

# Usando a função específica e corrigida para o gráfico logarítmico
print("Gerando gráfico logarítmico...")
plot_comparacao_log(dados_m1_log, dados_m2_log, "Comparação de Desempenho - Redução Logarítmica (O(log n))", "grafico_logaritmico.png")

# --- Gráfico comparativo geral foi removido ---
# A comparação por média foi removida por ser metodologicamente incorreta.
# Não é válido tirar a média de tempos de execução para escalas de INPUT tão diferentes
# (ex: 10.000 vs 1e50). A análise correta é feita pelos gráficos individuais.

print("\nGráficos salvos com sucesso:")
print("- grafico_linear.png")
print("- grafico_quadratico.png")
print("- grafico_logaritmico.png")