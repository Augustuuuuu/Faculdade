#include <stdio.h>
#include <locale.h>
#include <string.h>
// Versão01: Medir a maior e menor idade, e calcular a média das idades dos alunos
// Versão02: As medidas de tendencia central Moda e Mediana.
// Versão03: Solicitar ao usuário, alem das idades:
// O nome do aluno
// Sexo (M/F)
// As tres notas do aluno
// Ao final apresentar:
// Percentual de Alunos e Alunas aprovadas e reprovadas
// Percentuaç de Alunos aprovados/reprovados com mais de 20
// Relatório com os nomes e medias dos alunos aprovado e reprovados
// Configurar a media de aprovacao na faculdade e quantidade de provas
// Tratar entrada de dados nao permitido
// Genero diferente de M e F (tanto faz maisc e minusc)
// Idade <16 e nem > 100 anos (não pode)
// Nota menores que zero nem maiores que dez
// ---------------------------------------------------------------------------------------

struct Turma{
	char nome[100];
	int idade[100];
	int sexo;
	float notas[300];
};

int main(){
	
	setlocale(LC_ALL, "Portuguese"); // Console em Português
    float Maior, Menor;
    int Idade[100], Soma = 0;
    int Qtd = 0, resposta, sexo;
    char nome[100], nomeVelho[100] = "", nomeNovo[100] = "";
	struct Turma T = { Idade[100], nome[100]};
    do{
    	do{
        // Perguntando o nome e idade do aluno e fazendo a verificação caso a idade não seja válida
        printf("\n Informe o nome do %i. aluno: ", Qtd +1);
        scanf("%s", &T.nome);
        T.showName();
        printf("\n Informe a idade do %i. aluno: ", Qtd + 1);
        scanf("%d", &Idade[Qtd]);
        printf("\n Informe o sexo do aluno: "); scanf("%s", &sexo);
        if(Idade[Qtd] < 16 || Idade[Qtd] > 100){
        	printf("\nDigite uma idade válida! Entre 16 e 100\n");
		}
    	}while(Idade[Qtd] < 16 || Idade[Qtd] > 100);
    	// Acumulador para somar idade
        Soma += Idade[Qtd];

		// Verificando quem tem a menor idade e a maior
        if(Qtd == 0)
			{
        	Maior = Idade[0]; // Inicializar com zero para economizar uso de memória
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
        printf("\n Deseja informar o a próxima idade? 1/Sim - 2/Não ");
        scanf("%i", &resposta);
        Qtd ++;
    } while(resposta == 1);
    // Faça o algoritmo aqui
    
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


    // Saída de dados
    printf("\n O aluno mais velho se chama %s e tem %.0f anos.", nomeVelho, Maior);
    printf("\n O aluno mais novo se chama %s e tem %.0f anos.", nomeNovo, Menor);
    printf("\n Média de idade: %d", Soma / Qtd);
    printf("\n Mediana das idades: %d", mediana);

} 
