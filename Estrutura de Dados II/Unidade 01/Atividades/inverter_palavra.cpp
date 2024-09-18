#include <stdio.h>
#include <string.h>

int Tamanho(char S[]){
	int tamanho = strlen(S);
	return tamanho;
	
}

int main(){
	char palavra[60];
	scanf("%s", &palavra);
	
	for(int i = Tamanho(palavra)-1; i>=0; i--){
		printf("%c", palavra[i]);
		
	}
	
	
}
