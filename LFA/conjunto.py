# -*- coding: utf-8 -*-
"""
Programa: Operações com Conjuntos de Palavras
Autor: (Seu nome)
Descrição:
    Lê dois conjuntos de palavras (separadas por vírgula) e permite ao usuário
    escolher entre União (A ∪ B), Interseção (A ∩ B), Diferença (A − B) e Diferença (B − A).
Observação:
    As comparações são sensíveis a maiúsculas/minúsculas (e.g., 'Casa' != 'casa').
    Para ignorar diferenças de caixa, normalize as palavras com .lower() ou .casefold().
"""

def ler_conjunto(rotulo: str) -> set[str]:
    """
    Lê uma linha do usuário contendo palavras separadas por vírgula,
    remove espaços extras e entradas vazias, e devolve um conjunto (set).
    """
    entrada = input(f"Digite os elementos do conjunto {rotulo} separados por vírgula:\n> ")
    # Divide por vírgula, tira espaços nas pontas e ignora vazios
    itens = [p.strip() for p in entrada.split(",")]
    itens = [p for p in itens if p]  # remove strings vazias
    return set(itens)

def formatar_conjunto(s: set[str]) -> str:
    """
    Retorna uma representação legível do conjunto.
    Usa ordenação alfabética (case-insensitive para exibição).
    """
    if not s:
        return "∅"  # conjunto vazio
    ordenado = sorted(s, key=lambda x: (x.casefold(), x))
    return "{ " + ", ".join(ordenado) + " }"

def mostrar_menu() -> str:
    print("\nEscolha a operação que deseja realizar:")
    print("  1 → União (A ∪ B)        → todos os elementos de A e B")
    print("  2 → Interseção (A ∩ B)   → apenas os elementos em comum")
    print("  3 → Diferença (A − B)    → elementos que estão em A, mas não em B")
    print("  4 → Diferença (B − A)    → elementos que estão em B, mas não em A")
    opcao = input("Digite a opção (1-4): ").strip()
    return opcao

def main():
    print("=== Operações com Conjuntos de Palavras ===\n")
    A = ler_conjunto("A")
    B = ler_conjunto("B")

    print("\nVocê digitou:")
    print(f"A = {formatar_conjunto(A)}")
    print(f"B = {formatar_conjunto(B)}")

    opcao = mostrar_menu()
    while opcao not in {"1", "2", "3", "4"}:
        print("Opção inválida. Tente novamente.")
        opcao = mostrar_menu()

    if opcao == "1":
        resultado = A | B
        titulo = "União (A ∪ B)"
    elif opcao == "2":
        resultado = A & B
        titulo = "Interseção (A ∩ B)"
    elif opcao == "3":
        resultado = A - B
        titulo = "Diferença (A − B)"
    else:  # "4"
        resultado = B - A
        titulo = "Diferença (B − A)"

    print("\n==== Resultado ====")
    print(f"{titulo}: {formatar_conjunto(resultado)}")

    # Informações adicionais úteis (opcional)
    print("\nResumo:")
    print(f"|A| = {len(A)}  |B| = {len(B)}  |Resultado| = {len(resultado)}")
    print("\nObs.: As palavras são consideradas diferentes se houver diferença de maiúsculas/minúsculas.")

if __name__ == "__main__":
    main()
