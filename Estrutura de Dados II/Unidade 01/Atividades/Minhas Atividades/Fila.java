public class Fila {
private int total; //Total de Elementos
private int comeco; //Comeco da Fila
private int fim; //Final da Fila
private Object memo[]; //Vetor para armazenar os elementos
private int MAX; //Tamanho máximo da Fila Estática
//Inicializa a Fila em estado vazia
public Fila() {
MAX = 1000;
memo = new Object[MAX];
total = 0;
comeco = 0;
fim = 0;
}
//Verifica se Fila está vazia
public boolean qIsEmpty() {
return(total==0);
}
//Verifica se a Fila está cheia
private boolean qIsFull() {
return(total==MAX);
}
//Insere um elemento na Fila
public void enqueue(Object x) {
if(!qIsFull()) {
memo[fim++] = x;
fim %= MAX;
total++;
}
else
System.out.println("Fila Cheia!!");
}
//Remove um elemento do início da Fila
public Object dequeue() {
if(!qIsEmpty()) {
Object resp;
resp = memo[comeco++];
comeco %= MAX;
total--;
return resp;
}
else {
return null;
}
}
//Imprime o conteúdo da Fila
public void qPrint() {
int i;
if(!qIsEmpty()) {
String saida = "";
int cont = comeco;
for(i=0;i<total;i++) {
saida += memo[cont].toString() + ", ";
cont++;
cont %= MAX;
}
System.out.println("F:[ "+saida+" ]");
}
else
System.out.println("Fila Vazia");
}
}