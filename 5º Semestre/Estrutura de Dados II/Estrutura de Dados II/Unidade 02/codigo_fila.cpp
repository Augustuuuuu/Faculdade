#include<stdio.h>
#include <stdlib.h>
#include <locale.h>
struct Fila {
	int capacidade;
	float *dados;
	int primeiro;
	int ultimo;
	int nItens; 
};

void criarFila(struct Fila *f, int c) { 
	f->capacidade = c;
	f->dados = (float*) malloc (f->capacidade * sizeof(float));
	f->primeiro = 0;
	f->ultimo = -1;
	f->nItens = 0; 
}

void inserir(struct Fila *f, int v) {
	if(f->ultimo == f->capacidade-1) // Faz o check pra conferir se a lista passou da capcidade
		f->ultimo = -1;
	f->ultimo++;
	f->dados[f->ultimo] = v; // incrementa último e insere
	f->nItens++; // mais um item inserido
}

int remover(struct Fila *f) { // pega o item do começo da fila
	int temp = f->dados[f->primeiro++]; // pega o valor e incrementa o primeiro
	if(f->primeiro == f->capacidade) // 
		f->primeiro = 0;
	f->nItens--;  // um item retirado
	return temp;
}

int estaVazia(struct Fila *f) { // retorna verdadeiro se a fila está vazia
	return (f->nItens==0);
}

int estaCheia(struct Fila *f) { // retorna verdadeiro se a fila está cheia
	return (f->nItens == f->capacidade);
}

void mostrarFila(struct Fila *f){
	int cont, i;
	printf("[ ");
	for (cont=0, i= f->primeiro; cont < f->nItens; cont++){
		printf("%.2f ",f->dados[i++]);
		if (i == f->capacidade)
			i=0;
	}
	printf("]");
	printf("\n\n");
}

int main () {
	setlocale(LC_ALL, "Portuguese"); // Console em Português
	int opcao, capa;
	float valor;
	struct Fila umaFila;
	// cria a fila
	printf("\nCapacidade da fila? ");
	scanf("%d",&capa);
	criarFila(&umaFila, capa);
	// apresenta menu
	while(true){
		printf("\n1 - Inserir elemento\n2 - Remover elemento\n3 - Mostrar Fila\n0 - Sair\n\nOpção? ");
		scanf("%d", &opcao);
		switch(opcao){
			case 0: exit(0);
			case 1: // insere elemento
				if (estaCheia(&umaFila))
					printf("\nFila Cheia!!!\n\n");
				else {
					printf("\nValor do elemento a ser inserido? ");
					scanf("%f", &valor);
					inserir(&umaFila, valor);
					printf("\nElemento %.1f inserido na posição %d", valor, umaFila.ultimo);
				}
				break;
			case 2: // remove elemento
				if (estaVazia(&umaFila))
					printf("\nFila vazia!!!\n\n");
				else {
					valor = remover(&umaFila);
					printf("\n%.1f removido com sucesso\n\n", valor) ; 
				}
				break;
				case 3: // mostrar fila
					if (estaVazia(&umaFila)){
						printf("\nFila vazia!!!\n\n");
					}
					else {
						printf("\nConteúdo da fila => ");
						mostrarFila(&umaFila);
					}
					break;
				default:
					printf("\nOpção Inválida\n\n");
		}
	}
}
