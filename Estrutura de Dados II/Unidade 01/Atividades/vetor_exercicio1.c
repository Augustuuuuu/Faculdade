/* Escreva um algoritmo que solicite a quantidade de avaliações no semestres(entre uma e dez provas) notas de um aluno e ao final apresente se aprovado ou não conforme a média aritmética das N avaliações
1) Ao final apresenter a soma das notas e a média aritmética delas
2) Apresentar qual a avaliação que teve a maior nota(exemplo: A segunda prova teve a maior nota).
3) Apresentar qual a avaliação que teve a menor nota (exemplo: A primeira prova teve a menor nota).
4) Solicitar ao usuário no ínicio qual a média na faculdade para aprovação e informar se aprovado ou não. */
#include <locale.h>
#include <stdio.h>
#include <conio.h>
int main(){
    setlocale(LC_ALL, "Portuguese"); // Console em Português

    float nota[10], mediaFaculdade, maiorNota[1], menorNota[1];
    int i, qtdProvas;
    nota[0] = 0;
    // Atribuindo valor a variável mediaFaculdade
    printf("Informe a média de aprovação: ");
    scanf("%f", &mediaFaculdade);
    // Repetindo a variável qtdProvas até que as solicitações sejam atendidas
    do{
    printf("\n Informe a quantidade de provas: ");
    scanf("%i", &qtdProvas); 
    if (qtdProvas < 1 || qtdProvas >10)
        printf("\n Atenção!!! Entre UM e DEZ!!!"); }
    while (qtdProvas < 1 || qtdProvas >10);
    // Atribuindo valor ás qtdProvas usando o vetor nota[10]
    for (i=1; i<=qtdProvas; i++){
        printf(" Informe a %iº nota do aluno: ", i);
        scanf("%f", &nota[i]);
        nota[0] += nota[i]; // A primeira posição do vetor está acumulando a soma das notas
        if (i == 1){
        	maiorNota[0] = nota[i];
        	maiorNota[1] = i;
        	menorNota[0] = nota[i];
        	menorNota[1] = i;
		}
		else{
        	if (nota[i] >= maiorNota[0]){
        		maiorNota[0] = nota[i];
        		maiorNota[1] = i;
				}
			else if (nota[i] <= menorNota[0]){
        		menorNota[0] = nota[i];
        		menorNota[1] = i;
				}
			}
    }
	// Mostrando ao aluno se foi aprovado ou não baseado nas notas alcançadas e a média da faculdade
    if(nota[0] / qtdProvas >= mediaFaculdade){
        printf("\n Parabéns!!! Você foi aprovado com média %.2f.", nota[0] / qtdProvas);
    }
    else{
        printf("\n Infelizmente você não foi aprovado. Sua média foi de %.2f e você precisava de %.2f.",nota[0] / qtdProvas, mediaFaculdade);
    }
    
	// 2) Apresentar qual a avaliação que teve a maior nota(exemplo: A segunda prova teve a maior nota).
	printf("\n Relatório de provas");
	
	
    // 1) Ao final apresenter a soma das notas e a média aritmética delas
    printf("\n A %.0fº prova teve a maior nota. %.2f pontos", maiorNota[1], maiorNota[0]);
	printf("\n A %.0fº prova teve a menor nota. %.2f pontos", menorNota[1], menorNota[0]);
    printf("\n A soma das notas %.2f.", nota[0]);
    printf("\n A média das notas %.2f.", nota[0] / qtdProvas);

}