#include <stdio.h>
#include <locale.h>
// Escreva um algortimo que solicite ao usuário N valores númericos e ao final apresente:
// Versão01: O maior e o menor
// Versão02: As medidas de tendencia central Media, Moda e Mediana.
// Versão03: Implementar Nome, Idade, Sexo e Três notas dos alunos

int main(){
	
	setlocale(LC_ALL, "Portuguese"); // Console em Português
	    
    float Valor, Maior, Menor, Soma, Moda, Mediana, valores[100];
    int Qtd = 0, resposta, repeticao[100] = {0}, maior_repeticao = 0, i = 0;
    
    do{
        Qtd++;
        // Entrada de dados
        printf("\n Informe o %i. valor: ", Qtd);
        scanf("%f", &Valor);
        Soma += Valor;
        int valor_convertido = (int)Valor;
        repeticao[valor_convertido]++;
        // Processamento de dados
        valores[i++] = valor_convertido;
        
        
        if(Qtd ==1){
        	Maior = Valor;
        	Menor = Valor;
		}
		
        else if (Valor > Maior)
            Maior = Valor;
        else if(Valor < Menor)
            Menor = Valor;
                
        

        printf("\n Deseja informar o próximo valor? 1/Sim - 2/Não ");
        scanf("%i", &resposta);
    } while(resposta == 1);
    for (int i = 0; i < Qtd; i++){
        if (repeticao[i] > maior_repeticao){
            maior_repeticao = repeticao[i];
            Moda = i;
        }
    int meio = Qtd / 2;
    Mediana = (Qtd % 2 == 0) ? (valores[meio - 1] + valores[meio]) / 2.0 : valores[meio];
    }
    // Criar um vetor para verificar quais numeros se repetem enquanto o usuário informa
    // Saída de dados
    printf("\n O maior: %0.2f", Maior);
    printf("\n O menor: %0.2f", Menor);
    printf("\n Média: %0.2f", Soma / Qtd);
    printf("\n Moda: %0.2f", Moda);
    printf("\n Mediana: %0.2f", Mediana);
    
} 