
import matplotlib.pyplot as plt
from fpdf import FPDF

# Dados dos testes
passos = [100*i for i in range(1,21)]
tempos_soma = [0.000013,0.000010,0.000013,0.000017,0.000021,0.000025,0.000028,0.000032,0.000035,0.000056,
               0.000074,0.000079,0.000102,0.000101,0.002125,0.000104,0.000131,0.000130,0.000139,0.000192]

# 1️⃣ Gerar gráfico
plt.figure(figsize=(8,5))
plt.plot(passos, tempos_soma, marker='o', linestyle='-', color='blue', label='Soma simples')
plt.xlabel('Número de passos')
plt.ylabel('Tempo de execução (s)')
plt.title('Tempo de execução vs Número de passos - Soma simples')
plt.grid(True)
plt.legend()
plt.savefig('grafico_desempenho.png')
plt.close()

# 2️⃣ Criar PDF
pdf = FPDF()
pdf.add_page()

# Capa
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Análise de Desempenho de Algoritmos em Python", 0, 1, "C")
pdf.ln(5)

# Resumo
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, ("Resumo:\n"
                       "Este relatório compara o desempenho de algoritmos em Python. "
                       "O objetivo é analisar os tempos de execução e identificar padrões na relação "
                       "entre o tamanho da entrada (número de passos) e o tempo de processamento. "
                       "O algoritmo testado aqui é uma soma simples que soma todos os números de 1 até n."))

pdf.ln(5)

# Especificações do sistema
pdf.multi_cell(0, 8, ("Especificações do sistema:\n"
                       "Sistema Operacional: Windows 11 (10.0.26100)\n"
                       "Processador: 12th Gen Intel(R) Core(TM) i5-1235U\n"
                       "Núcleos físicos: 10\n"
                       "Núcleos lógicos: 12\n"
                       "Memória total: 7.71 GB"))

pdf.ln(5)

# Tabela de resultados
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "Resultados dos testes:", 0, 1)
pdf.set_font("Arial", "", 10)

pdf.cell(20, 8, "Teste", 1)
pdf.cell(40, 8, "Número de passos", 1)
pdf.cell(40, 8, "Tempo (s)", 1)
pdf.ln()

for i, (passo, tempo) in enumerate(zip(passos, tempos_soma)):
    pdf.cell(20, 8, str(i+1), 1)
    pdf.cell(40, 8, str(passo), 1)
    pdf.cell(40, 8, f"{tempo:.6f}", 1)
    pdf.ln()

pdf.ln(5)

# Inserir gráfico
pdf.image("grafico_desempenho.png", x=10, w=180)

pdf.ln(5)

# Análise comparativa
pdf.multi_cell(0, 8, ("Análise comparativa:\n"
                       "O crescimento do tempo de execução não é perfeitamente linear. "
                       "Para valores pequenos, o tempo é quase constante, mas ao aumentar o número de passos, "
                       "o tempo começa a crescer de forma não linear, evidenciando uma redução não linear "
                       "em relação à proporcionalidade direta entre passos e tempo."))

pdf.ln(5)

# Conclusão
pdf.multi_cell(0, 8, ("Conclusão:\n"
                       "O algoritmo de soma simples apresenta crescimento de tempo muito baixo para pequenas entradas, "
                       "mas com entradas maiores observa-se um aumento mais perceptível, caracterizando um padrão "
                       "de crescimento não linear. Este comportamento deve ser considerado em análises de desempenho "
                       "de algoritmos para entradas grandes."))

# Salvar PDF
pdf.output("relatorio_algoritmo_soma.pdf")
print("PDF gerado com sucesso: relatorio_algoritmo_soma.pdf")
