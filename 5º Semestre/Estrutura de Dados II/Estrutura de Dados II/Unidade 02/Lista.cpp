#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
struct Node {
    int data;
    struct Node* next;
};

// Fun��o para criar um novo n�
struct Node* newNode(int data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

// Fun��o para inserir um n� no in�cio da lista
void adicionar_inicio(struct Node** head_ref, int new_data) {
    struct Node* new_node = newNode(new_data);
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

// Fun��o para imprimir a lista
void imprimir_lista(struct Node* n) {
    while (n != NULL) {
        printf("%d ", n->data);
        n = n->next;
    }
}


int main(){
	setlocale(LC_ALL, "Portuguese"); // Console em Portugu�s
    struct Node* lista = NULL;
    int opcao, valor;

    do {
        printf("\nMenu:\n");
        printf("1. Inserir valor\n");
        printf("2. Imprimir lista\n");
        printf("3. Sair\n");
        printf("Escolha uma op��o: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &valor);
                adicionar_inicio(&lista, valor);
                break;
            case 2:
                imprimir_lista(lista);
                break;
            case 3:
                printf("Saindo...\n");
                break;
            default:
                printf("Op��o inv�lida!\n");
        }
    } while (opcao != 3);

    return 0;
}

