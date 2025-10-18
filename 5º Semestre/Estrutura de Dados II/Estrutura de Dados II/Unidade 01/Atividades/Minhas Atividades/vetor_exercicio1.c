/* Escreva um algoritmo que solicite a quantidade de avalia��es no semestres(entre uma e dez provas) notas de um aluno e ao final apresente se aprovado ou n�o conforme a m�dia aritm�tica das N avalia��es
1) Ao final apresenter a soma das notas e a m�dia aritm�tica delas
2) Apresentar qual a avalia��o que teve a maior nota(exemplo: A segunda prova teve a maior nota).
3) Apresentar qual a avalia��o que teve a menor nota (exemplo: A primeira prova teve a menor nota).
4) Solicitar ao usu�rio no �nicio qual a m�dia na faculdade para aprova��o e informar se aprovado ou n�o. */
#include <locale.h>
#include <stdio.h>
#include <conio.h>
int main(){
    setlocale(LC_ALL, "Portuguese"); // Console em Portugu�s

    float nota[10], mediaFaculdade, maiorNota[1], menorNota[1];
    int i, qtdProvas;
    nota[0] = 0;
    // Atribuindo valor a vari�vel mediaFaculdade
    printf("Informe a m�dia de aprova��o: ");
    scanf("%f", &mediaFaculdade);
    // Repetindo a vari�vel qtdProvas at� que as solicita��es sejam atendidas
    do{
    printf("\n Informe a quantidade de provas: ");
    scanf("%i", &qtdProvas); 
    if (qtdProvas < 1 || qtdProvas >10)
        printf("\n Aten��o!!! Entre UM e DEZ!!!"); }
    while (qtdProvas < 1 || qtdProvas >10);
    // Atribuindo valor �s qtdProvas usando o vetor nota[10]
    for (i=1; i<=qtdProvas; i++){
        printf(" Informe a %i� nota do aluno: ", i);
        scanf("%f", &nota[i]);
        nota[0] += nota[i]; // A primeira posi��o do vetor est� acumulando a soma das notas
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
	// Mostrando ao aluno se foi aprovado ou n�o baseado nas notas alcan�adas e a m�dia da faculdade
    if(nota[0] / qtdProvas >= mediaFaculdade){
        printf("\n Parab�ns!!! Voc� foi aprovado com m�dia %.2f.", nota[0] / qtdProvas);
    }
    else{
        printf("\n Infelizmente voc� n�o foi aprovado. Sua m�dia foi de %.2f e voc� precisava de %.2f.",nota[0] / qtdProvas, mediaFaculdade);
    }
    
	// 2) Apresentar qual a avalia��o que teve a maior nota(exemplo: A segunda prova teve a maior nota).
	printf("\n Relat�rio de provas");
	
	
    // 1) Ao final apresenter a soma das notas e a m�dia aritm�tica delas
    printf("\n A %.0f� prova teve a maior nota. %.2f pontos", maiorNota[1], maiorNota[0]);
	printf("\n A %.0f� prova teve a menor nota. %.2f pontos", menorNota[1], menorNota[0]);
    printf("\n A soma das notas %.2f.", nota[0]);
    printf("\n A m�dia das notas %.2f.", nota[0] / qtdProvas);

}
