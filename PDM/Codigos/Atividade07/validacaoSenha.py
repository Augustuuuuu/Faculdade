def valida_senha_q0_q3(senha: str) -> bool:
    """
    Implementação do autômato pedido:
    q0 = Entrada (leitura)
    q1 = Verificar letra maiúscula (flag tem_maiuscula)
    q2 = Conter número (flag tem_numero)
    q3 = Terminar com símbolo especial (flag ultimo_eh_simbolo)
    q4 = Aceita
    q5 = Rejeita
    """

    # Estado inicial
    estado = "q0"
    print(f"Estado {estado}: Iniciando leitura da senha '{senha}'")

    # Flags correspondentes aos estados q1, q2, q3
    tem_maiuscula = False  # q1
    tem_numero = False     # q2
    ultimo_eh_simbolo = False  # q3 (depende do último caractere lido)

    # Leitura caractere a caractere (permanece em q0 enquanto lê)
    for ch in senha:
        # categoria: maiúscula?
        if ch.isupper():
            tem_maiuscula = True
            ultimo_eh_simbolo = False
            print(f"  Leu '{ch}': é MAIÚSCULA -> tem_maiuscula = True, ultimo_eh_simbolo = False")
            continue

        # categoria: minúscula?
        if ch.islower():
            # nenhuma nova flag além de limpar ultimo_eh_simbolo
            ultimo_eh_simbolo = False
            print(f"  Leu '{ch}': é minúscula -> sem flags novas, ultimo_eh_simbolo = False")
            continue

        # categoria: dígito?
        if ch.isdigit():
            tem_numero = True
            ultimo_eh_simbolo = False
            print(f"  Leu '{ch}': é DÍGITO -> tem_numero = True, ultimo_eh_simbolo = False")
            continue

        # categoria: símbolo especial (não alfanumérico)
        if not ch.isalnum():
            # neste ponto, marcamos que o último caractere é símbolo
            ultimo_eh_simbolo = True
            print(f"  Leu '{ch}': é SÍMBOLO ESPECIAL -> ultimo_eh_simbolo = True")
            continue

        # Caso (teórico) de caractere não categorizado
        ultimo_eh_simbolo = False
        print(f"  Leu '{ch}': caractere não categorizado, ultimo_eh_simbolo = False")

    # Fim da leitura: decidir
    print("Fim da leitura. Resumo das flags:")
    print(f"  tem_maiuscula = {tem_maiuscula}")
    print(f"  tem_numero = {tem_numero}")
    print(f"  ultimo_eh_simbolo = {ultimo_eh_simbolo}")

    # transição final a partir de q0
    if tem_maiuscula and tem_numero and ultimo_eh_simbolo:
        estado = "q4"  # ACEITA
        print(f"Transição final: q0 -> {estado} (ACEITA)")
        return True
    else:
        estado = "q5"  # REJEITA
        print(f"Transição final: q0 -> {estado} (REJEITA)")
        return False


# -----------------------
# Testes solicitados (pelo menos 2 aceitos e 1 rejeitado)
tests = [
    ("Senha1@", True),    # tem maiúscula 'S', tem número '1', termina com '@' -> ACEITA
    ("A2$", True),        # tem maiúscula 'A', tem número '2', termina com '$' -> ACEITA
    ("senha1!", False),   # não tem maiúscula -> REJEITA
    # exemplos adicionais:
    ("Abc1", False),      # termina sem símbolo especial -> REJEITA
    ("1#A", True),        # maiúscula 'A', número '1', termina com '#' -> ACEITA
]

print("\n--- Início dos testes ---\n")
for s, esperado in tests:
    print(f"Testando: '{s}' (esperado: {esperado})")
    resultado = valida_senha_q0_q3(s)
    print(f"Resultado obtido: {resultado}")
    print("--------------\n")
print("--- Fim dos testes ---")
