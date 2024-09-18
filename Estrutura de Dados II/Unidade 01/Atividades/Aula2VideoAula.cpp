/* Exercício utilizando estruturas em Linguagem de programação C++ */
// 	Medir a maior e menor idade, e calcular a média das idades dos alunos
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
#include <stdio.h>
#include <locale.h>
#include <string.h>
struct Aluno{
	char Nome[30];
	char sexo;
	int Idade;
	float Nota;
};



int main(){
	setlocale(LC_ALL, "Portuguese"); // Console em Português
	struct Aluno vetorAluno[100];
	int qtd, i, maiorIdade, menorIdade; char resposta, nomeVelho[30], nomeNovo[30];
	
	printf("\n Informe a quantidade de alunos: "); scanf("%d", &qtd);
	for (i = 0; i < qtd; i++){ // Inicio do loop
		
	printf("\n Informe o nome do %d. aluno: ", i+1); scanf(" %[^\n]s", &vetorAluno[i].Nome);
	printf("\n Informe a idade de %s: ", vetorAluno[i].Nome); scanf("%d", &vetorAluno[i].Idade);
	printf("\n Informe a nota de %s: ", vetorAluno[i].Nome); scanf("%f", &vetorAluno[i].Nota);
	// Escrever aqui as formulas para os pedidos do exercício
	
	// Verificando o nome e idade do aluno mais velho e mais novo
	if (i == 0) {
    maiorIdade = vetorAluno[i].Idade;
    menorIdade = vetorAluno[0].Idade;
    strcpy(nomeVelho, vetorAluno[i].Nome); // Copia o nome para nomeVelho
    strcpy(nomeNovo, vetorAluno[i].Nome); // Copia o nome para nomeNovo
	} else if (vetorAluno[i].Idade > maiorIdade) {
    maiorIdade = vetorAluno[i].Idade;
    strcpy(nomeVelho, vetorAluno[i].Nome);
	} else if (vetorAluno[i].Idade < menorIdade) {
    menorIdade = vetorAluno[i].Idade;
    strcpy(nomeNovo, vetorAluno[i].Nome);
}




} // Fim do loop
	
	printf("%s é o aluno mais velho com %d anos.", nomeVelho, maiorIdade);
	printf("%s é o aluno mais novo com %d anos.", nomeNovo, menorIdade);
	
}
