#include <stdio.h>
#include <locale.h>
#include <string.h>
// 	Medir a maior e menor idade, e calcular a m�dia das idades dos alunos  = FEITO
// Vers�o02: As medidas de tendencia central Moda e Mediana.
// Vers�o03: Solicitar ao usu�rio, alem das idades:
// O nome do aluno  = FEITO
// Sexo (M/F) = FEITO
// As tres notas do aluno = FEITO
// Ao final apresentar:
// Percentual de Alunos e Alunas aprovadas e reprovadas
// Percentua� de Alunos aprovados/reprovados com mais de 20
// Relat�rio com os nomes e medias dos alunos aprovado e reprovados
// Configurar a media de aprovacao na faculdade e quantidade de provas
// Tratar entrada de dados nao permitido
// Genero diferente de M e F (tanto faz maisc e minusc)
// Idade <16 e nem > 100 anos (n�o pode)
// Nota menores que zero nem maiores que dez
// ---------------------------------------------------------------------------------------

struct Turma{
	char nome[100];
	int idade[100];
	int sexo;
	float notas[300];
};

int main(){
	
	setlocale(LC_ALL, "Portuguese"); // Console em Portugu�s
    float Maior, Menor;
    int Idade[100], Soma = 0;	
    float notas[100], SomaNotas = 0;
    int Qtd = 0, resposta, sexo;
    char nome[100], nomeVelho[100] = "", nomeNovo[100] = "";
	struct Turma T = { Idade[100], nome[100], notas[100]};
    do{
    	do{
        // Perguntando o nome e idade do aluno e fazendo a verifica��o caso a idade n�o seja v�lida
        printf("\n Informe o nome do %i. aluno: ", Qtd +1);
        scanf("%s", &T.nome);
        printf("\n Informe a idade do %i. aluno: ", Qtd + 1);
        scanf("%d", &Idade[Qtd]);
        printf("\n Informe o sexo do aluno: "); scanf("%s", &sexo);
        if(Idade[Qtd] < 16 || Idade[Qtd] > 100){
        	printf("\nDigite uma idade v�lida! Entre 16 e 100\n");
		}
    	}while(Idade[Qtd] < 16 || Idade[Qtd] > 100);
    	// Acumulador para somar idade
        Soma += Idade[Qtd];

		// Verificando quem tem a menor idade e a maior
        if(Qtd == 0)
			{
        	Maior = Idade[0]; // Inicializar com zero para economizar uso de mem�ria
        	Menor = Idade[0];
        	strcpy(nomeVelho, T.nome); // Inicializa nomeVelho com o primeiro nome
        	strcpy(nomeNovo, T.nome);
			}
        else if (Idade[Qtd] > Maior)
        	{
            Maior = Idade[Qtd];
            strcpy(nomeVelho, T.nome);
        	}
        else if(Idade[Qtd] < Menor)
			{
            Menor = Idade[Qtd];
            strcpy(nomeNovo, T.nome);
    		}
    	
    	for(int i = 0; i < 3; i++){
    		printf("\n Digite a %d. nota: ", i); scanf("%f", &T.notas[i]);
    		SomaNotas += T.notas[i];
		}
    		
        printf("\n Deseja informar o pr�xima aluno? 1/Sim - 2/N�o ");
        scanf("%i", &resposta);
        Qtd ++;
    } while(resposta == 1);
    // Fa�a o algoritmo aqui
    
    // Bubble sort para ordenar as idades
    int i, j, temp;
    for (i = 0; i < Qtd - 1; i++) {
        for (j = 0; j < Qtd - i - 1; j++) {
            if (Idade[j] > Idade[j + 1]) {
                temp = Idade[j];
                Idade[j] = Idade[j + 1];
                Idade[j + 1] = temp;
            }
        }
    }

    // Encontrar a mediana
    int mediana;
    if (Qtd % 2 == 0) { // Se a amostra for par tem que pegar a media aritmetica dos numeros centrais
        mediana = (Idade[Qtd / 2 - 1] + Idade[Qtd / 2]) / 2;
    } else {
        mediana = Idade[Qtd / 2]; // Se for impar elemento do centro
    }


    // Sa�da de dados
    printf("\n O aluno mais velho se chama %s e tem %.0f anos.", nomeVelho, Maior);
    printf("\n O aluno mais novo se chama %s e tem %.0f anos.", nomeNovo, Menor);
    printf("\n M�dia de idade: %d", Soma / Qtd);
    printf("\n Mediana das idades: %d", mediana);
	printf("\n M�dia das notas %.2f", SomaNotas/ 3);
} 
