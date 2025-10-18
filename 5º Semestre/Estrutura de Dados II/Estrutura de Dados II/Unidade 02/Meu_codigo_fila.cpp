#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

struct T_QUEUE{
	int dados;
	int fim;	
};

void startQueue(T_QUEUE *f, int N){
	int i;
	for(i=0;i<N;i++){
		f->dados[i] = 0;
	}
	f->fim = 0;
}

void enqueue(int dado, T_QUEUE *f){
	if(f->fim == N){
		printf("\n Fila esta cheia!");
		return;
	}
	else{
		f->dados[f->fim] = dado;
		f->fim++;
	}
}

int dequeue(T_QUEUE *f){
	int dado,i;
	if(f->fim == 0){
		printf("\n Fila esta vazia!");
		return dado;
	}
	else{
		dado = f->dados[0];
		for(i=0;i<f->fim;i++){
			f->dados[i] = f->dados[i+1];
		}
		f->fim--;
		return dado;
	}
}


void showQueue(T_QUEUE *f){
	int i;
	printf("\n Imprimindo a fila: ");
	for(i=0; i<f->fim;i++){
		printf("%d ", f->dados[i]);
	}
}

void empty(T_QUEUE *f){
	if(f->dados)
}
int main(){
	int sizeofqueue;
	T_QUEUE f1;
	
	printf("\n Informe o tamanho da fila: "); scanf("%d", sizeofqueue);
	
	startQueue(&f1);

	showQueue(&f1);
}

