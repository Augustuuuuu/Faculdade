import sys

def reconhece_comentario_java(entrada: str) -> bool:
    """
    Simulador de Autômato Finito para reconhecer comentários de linha Java (//...).
    
    Este autômato segue as regras:
    1. Deve começar com "//".
    2. Pode ter qualquer caractere depois, exceto quebra de linha.
    3. Termina com quebra de linha ('\n') ou o fim da entrada.
    """
    
    # --- Definição do Autômato ---
    
    # Estados:
    Q0 = 0  # Estado inicial
    Q1 = 1  # Viu o primeiro caractere '/'
    Q2 = 2  # Viu '//' (dentro de um comentário)
    Q3 = 3  # Estado final (viu '\n' após Q2)
    Q4 = 4  # Estado de erro/rejeição (armadilha)
    
    # Estado inicial
    estado_atual = Q0
    
    # Conjunto de estados finais formais (apenas Q3)
    estados_finais_formais = {Q3}
    
    # --- Processamento da Cadeia de Entrada ---
    
    # Itera por cada caractere da string de entrada
    for char in entrada:
        
        # Estado Q0 (Inicial)
        if estado_atual == Q0:
            if char == '/':
                estado_atual = Q1  # Transição: Q0 -> Q1
            else:
                estado_atual = Q4  # Inválido: não começou com '/'
        
        # Estado Q1 (Viu a primeira barra '/')
        elif estado_atual == Q1:
            if char == '/':
                estado_atual = Q2  # Transição: Q1 -> Q2 (confirmou '//')
            else:
                estado_atual = Q4  # Inválido: não era '//'
        
        # Estado Q2 (Dentro do comentário '//...')
        elif estado_atual == Q2:
            if char == '\n':
                estado_atual = Q3  # Transição: Q2 -> Q3 (fim da linha)
            else:
                # Qualquer outro caractere é parte do comentário
                estado_atual = Q2  # Permanece em Q2
        
        # Estado Q3 (Fim da linha, Aceitação)
        elif estado_atual == Q3:
            # Se a string continuar *após* o \n, ela é inválida
            estado_atual = Q4  # Inválido: lixo após o fim da linha
        
        # Estado Q4 (Erro/Armadilha)
        elif estado_atual == Q4:
            # Uma vez no estado de erro, permanece nele
            estado_atual = Q4 
            
    # --- Verificação Final (Após processar a string inteira) ---
    
    # A entrada é aceita se o autômato parou em:
    # 1. Q2 (regra "fim da entrada")
    # 2. Q3 (regra "termina com quebra de linha")
    
    return estado_atual == Q2 or estado_atual in estados_finais_formais

# --- Execução dos Casos de Teste ---

if __name__ == "__main__":
    
    # Lista de entradas que o autômato DEVE aceitar
    casos_aceitos = [
        "// Este é um comentário válido",  # Aceito (regra "fim da entrada" em Q2)
        "//Comentário sem espaço\n",     # Aceito (transição para Q3)
        "// TODO: implementar método",  # Aceito (regra "fim de entrada" em Q2)
        "//",                           # Aceito (fim de entrada em Q2)
        "//\n",                         # Aceito (transição para Q3)
    ]
    
    # Lista de entradas que o autômato DEVE rejeitar
    casos_rejeitados = [
        "/ comentário inválido",        # Rejeitado (erro em Q1)
        "/* comentário de bloco */",   # Rejeitado (erro em Q1)
        "texto antes // comentário",     # Rejeitado (erro em Q0)
        "// válido\nmas com lixo depois", # Rejeitado (erro em Q3)
    ]
    
    print("Executando Casos de Teste do Autômato:\n")
    
    total_corretos = 0
    total_testes = len(casos_aceitos) + len(casos_rejeitados)
    
    # --- Testa os Casos de Aceitação ---
    print("--- Casos de Aceitação (Esperado: True) ---")
    for entrada in casos_aceitos:
        resultado = reconhece_comentario_java(entrada)
        esperado = True  # Para esta lista, o esperado é sempre True
        
        status = "PASSOU" if resultado == esperado else "FALHOU"
        if resultado == esperado:
            total_corretos += 1
            
        print(f"[{status: <7}] Entrada: '{entrada.replace('\n', '\\n')}'")
        print(f"          Esperado: {esperado}, Recebido: {resultado}\n")

    # --- Testa os Casos de Rejeição ---
    print("--- Casos de Rejeição (Esperado: False) ---")
    for entrada in casos_rejeitados:
        resultado = reconhece_comentario_java(entrada)
        esperado = False # Para esta lista, o esperado é sempre False
        
        status = "PASSOU" if resultado == esperado else "FALHOU"
        if resultado == esperado:
            total_corretos += 1
            
        print(f"[{status: <7}] Entrada: '{entrada.replace('\n', '\\n')}'")
        print(f"          Esperado: {esperado}, Recebido: {resultado}\n")

    # --- Sumário Final ---
    print("-" * 40)
    print(f"Resultado: {total_corretos} de {total_testes} casos corretos.")