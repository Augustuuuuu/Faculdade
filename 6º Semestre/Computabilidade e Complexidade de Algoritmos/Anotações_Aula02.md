# 📝 Anotações Relevantes: Computabilidade - Aula 2

## **1. A Importância de Medir a Eficiência de Algoritmos**

* Algoritmos eficientes são tão importantes quanto hardware potente. Muitas vezes, o algoritmo correto supera o impacto de ter máquinas mais rápidas.
* Para volumes grandes de dados, um algoritmo eficiente pode reduzir drasticamente o tempo de processamento e custo computacional.
* Melhorias na eficiência algorítmica traduzem-se em economia de recursos, energia e tempo.

## **2. Como Medir a Eficiência: Contagem de Passos**

* "Passos" são operações elementares executadas pelo algoritmo, como:

  * Atribuições de variáveis.
  * Comparações lógicas.
  * Operações aritméticas básicas.
  * Acessos à memória (leitura/escrita).
* Vantagens da contagem de passos:

  * É uma medida independente do hardware específico.
  * Permite uma comparação objetiva entre algoritmos.
  * Foca no comportamento à medida que a entrada (n) cresce.
  * Ajuda a identificar gargalos e oportunidades de otimização.

### **Exemplos em python:**

```python-repl
import os
os.system('cls' if os.name == 'nt' else 'clear')
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, j)
```

Para n = 5, temos:
5 * 2 / 2 = 15 execuções
Portanto, a complexidade é O(n²), mesmo sendo menos execuções que um loop duplo completo (n²).

## **3. Por que a Contagem de Passos é Melhor que Medir em "Segundos"?**

* O tempo real de execução varia dependendo de fatores como hardware (processador, memória, cache), sistema operacional, e compilador.
* A contagem de passos é uma métrica portável e comparável entre diferentes ambientes.
* Medidas de tempo em segundos são úteis como experimentos para validar análises teóricas, desde que realizadas na mesma máquina e condições.

### **Medindo o tempo de execução:**

Utilizando time.time() em Python

```
import os, time
os.system('cls' if os.name == 'nt' else 'clear')
n = 100000
inicio = time.time()
soma = 0
for i in range(n):
    soma += i
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} s")
print(f"Soma total = {soma}")
```

**Esta abordagem é útil para comparar algoritmos executados na mesma máquina, complementando a análise teórica com dados reais.**

## **4. Ordem de Crescimento e Notação Big-O**

* A ordem de crescimento descreve como o número de passos de um algoritmo aumenta em relação ao tamanho da entrada (n), especialmente quando n é grande.
* As características principais da análise de ordem de crescimento são:
  * Focar no comportamento para n grande.
  * Ignorar constantes multiplicativas.
  * Considerar apenas o termo de maior crescimento.
* A Notação Big-O é uma forma matemática de descrever o crescimento do tempo de execução de um algoritmo em função do tamanho da entrada n, quando n fica muito grande.
* **$O(g(n))$** representa um limite superior para o crescimento de uma função quando n é suficientemente grande.
* A análise com Big-O descreve o limite superior ou o pior cenário, ignora constantes e termos de menor ordem, e foca na taxa de crescimento em vez de segundos exatos. Um crescimento menor indica um algoritmo mais escalável.

## **5. Classes Comuns de Complexidade**

| Notação                 | Nome         | Descrição                                                                                                            | Exemplo                                               |
| :------------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| **$O(1)$**        | Constante    | O tempo de execução é fixo, independente do tamanho da entrada.                                                     | Acessar um elemento em um array.                      |
| **$O(\log n)$**   | Logarítmica | O tempo de execução cresce muito lentamente com o tamanho da entrada, tipicamente ao dividir o problema pela metade. | Busca binária.                                       |
| **$O(n)$**        | Linear       | O tempo de execução cresce proporcionalmente ao tamanho da entrada.                                                  | Percorrer todos os elementos de uma lista.            |
| **$O(n \log n)$** | Quase-linear | Um crescimento um pouco maior que o linear, comum em algoritmos eficientes de ordenação.                             | Merge sort, Quick sort (caso médio).                 |
| **$O(n^2)$**      | Quadrática  | O tempo de execução cresce ao quadrado do tamanho da entrada, geralmente devido a loops aninhados.                   | Dois loops aninhados iterando sobre a mesma entrada.  |
| **$O(2^n)$**      | Exponencial  | O tempo de execução dobra a cada adição à entrada, tornando-o inviável para grandes volumes de dados.            | Resolver o problema de subconjuntos por força bruta. |
