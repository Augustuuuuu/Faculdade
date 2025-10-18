#include <stdio.h>
#include <string.h>
struct Turma{
public:
	Aluno(){
		nome = "Augusto";
		idade = 0;
		sexo = "m";
	}
	Notas(){
		notas = 0;
	}
	void showId(){
		printf("%s", nome);
		printf("%d", idade);
		printf("%d", sexo);
	}
};
int main(){
	char nome[100];
	int idade, sexo;
	
	Turma novaturma("Augusto", 18, "f");
	
}
