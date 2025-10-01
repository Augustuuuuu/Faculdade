import pandas as pd

# --- Dados dos Jobs (Tabela da Página 12) ---
# Cada job é um dicionário com suas propriedades, facilitando o acesso aos dados.
jobs_data = {
    'J1': {'Grupo': 'A', 'Tempo': 10, 'Prioridade': 'Alta', 'Receita': 500, 'Deadline': 40, 'Lambda': 15},
    'J2': {'Grupo': 'B', 'Tempo': 15, 'Prioridade': 'Média', 'Receita': 400, 'Deadline': 70, 'Lambda': 8},
    'J3': {'Grupo': 'A', 'Tempo': 20, 'Prioridade': 'Alta', 'Receita': 700, 'Deadline': 60, 'Lambda': 18},
    'J4': {'Grupo': 'B', 'Tempo': 8, 'Prioridade': 'Baixa', 'Receita': 200, 'Deadline': 120, 'Lambda': 4},
    'J5': {'Grupo': 'A', 'Tempo': 12, 'Prioridade': 'Média', 'Receita': 450, 'Deadline': 80, 'Lambda': 10},
}

# --- Regras de Negócio do Sistema (Página 13) ---
# As regras são armazenadas em estruturas de dados para fácil consulta e modificação.
REGRAS_SLA = {
    'Alta': {'Limite': 15, 'Penalidade': 400},
    'Média': {'Limite': 30, 'Penalidade': 150},
    'Baixa': {'Limite': 60, 'Penalidade': 50}
}

CUSTO_SETUP = {'Tempo': 3, 'Custo': 30}
CUSTO_OCIOSIDADE_POR_MINUTO = 5

def analisar_rota(rota, jobs, regras_sla, custo_setup, verbose=True):
    tempo_atual = 0
    grupo_anterior = None
    receita_bruta = 0
    custos_totais = {
        'Setup': 0,
        'SLA': 0,
        'Deadline': 0,
        'Ociosidade': 0 # Reservado para cálculos de ociosidade
    }

    detalhes_calculo = []

    for job_id in rota:
        job = jobs[job_id]
        
        # 1. Verifica e aplica custo de Setup se houver troca de grupo
        custo_setup_rodada = 0
        if grupo_anterior is not None and grupo_anterior != job['Grupo']:
            tempo_atual += custo_setup['Tempo']
            custos_totais['Setup'] += custo_setup['Custo']
            custo_setup_rodada = custo_setup['Custo']
        
        tempo_inicio = tempo_atual

        # 2. Verifica violação de SLA e aplica penalidade
        penalidade_sla_rodada = 0
        sla = regras_sla[job['Prioridade']]
        if tempo_inicio > sla['Limite']:
            custos_totais['SLA'] += sla['Penalidade']
            penalidade_sla_rodada = sla['Penalidade']

        # 3. Processa o job, avançando o tempo
        tempo_termino = tempo_inicio + job['Tempo']
        tempo_atual = tempo_termino

        # 4. Verifica atraso de Deadline e aplica penalidade
        penalidade_deadline_rodada = 0
        if tempo_termino > job['Deadline']:
            atraso = tempo_termino - job['Deadline']
            penalidade = atraso * job['Lambda']
            custos_totais['Deadline'] += penalidade
            penalidade_deadline_rodada = penalidade

        # 5. Adiciona a receita do job
        receita_bruta += job['Receita']
        
        # Guarda os detalhes desta etapa
        detalhes_calculo.append({
            'Job': job_id, 'Grupo': job['Grupo'], 'Tempo Início': tempo_inicio,
            'Tempo Final': tempo_termino, 'Custo Setup': custo_setup_rodada,
            'Penalidade SLA': penalidade_sla_rodada,
            'Penalidade Deadline': penalidade_deadline_rodada, 'Receita': job['Receita']
        })
        
        grupo_anterior = job['Grupo']

    lucro_liquido = receita_bruta - sum(custos_totais.values())
    
    df_detalhes = pd.DataFrame(detalhes_calculo)

    # Imprime os resultados formatados se verbose for True
    if verbose:
        print("--- Análise da Rota ---")
        print(f"Rota Analisada: {' -> '.join(rota)}")
        print("\n--- Detalhes por Job ---")
        print(df_detalhes.to_string(index=False))
        print("\n--- Resumo Financeiro ---")
        print(f"Receita Bruta Total: R$ {receita_bruta:,.2f}")
        print(f"  - Custo de Setup: R$ {custos_totais['Setup']:,.2f}")
        print(f"  - Penalidades de SLA: R$ {custos_totais['SLA']:,.2f}")
        print(f"  - Penalidades de Deadline: R$ {custos_totais['Deadline']:,.2f}")
        print("---------------------------------")
        print(f"LUCRO LÍQUIDO: R$ {lucro_liquido:,.2f}")
        print(f"Tempo Total de Execução: {tempo_atual} minutos")

    return lucro_liquido, df_detalhes

# --- Como Usar o Código ---
if __name__ == "__main__":
    # Para testar uma rota diferente, basta modificar a lista abaixo
    rota_para_analisar = ['J1', 'J3', 'J5', 'J2', 'J4']
    
    # Chama a função principal para executar a análise
    analisar_rota(rota_para_analisar, jobs_data, REGRAS_SLA, CUSTO_SETUP)