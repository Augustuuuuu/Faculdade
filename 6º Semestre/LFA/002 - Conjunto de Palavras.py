def MenuOpcoes():
    print('+--------------------------------------------------------------------+')
    print('|             Selecione a opção que deseja executar                  |')
    print('|                                                                    |')
    print('|   [1] - União                            [2] - Interseção          |')
    print('|   [3] - Diferença (A - B)                [4] - Diferença (B - A)   |')
    print('|                                                                    |')
    print('+--------------------------------------------------------------------+')


def ler_conjunto(nome):
    while True:
        try:
            qnt = int(input(f'Informe quantas palavras deseja inserir no conjunto {nome}: '))
            break
        except ValueError:
            print('Valor inválido')

    conjunto = set()
    for i in range(qnt):
        conjunto.add(input(f'Insira a {i+1}° palavra do conjunto {nome}: '))
    return conjunto


def main():
    A = ler_conjunto("A")
    B = ler_conjunto("B")

    print(f"\nConjunto A: {A}")
    print(f"Conjunto B: {B}")

    MenuOpcoes()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("União:", A | B)
    elif opcao == "2":
        print("Interseção:", A & B)
    elif opcao == "3":
        print("Diferença (A - B):", A - B)
    elif opcao == "4":
        print("Diferença (B - A):", B - A)
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
