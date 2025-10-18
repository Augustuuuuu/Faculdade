# 🧠 Anotações de Computabilidade e Complexidade

## 📈 **Parte 1: Análise de Algoritmos**

A análise de algoritmos é o estudo sistemático do desempenho de um algoritmo, focando em dois recursos críticos: **tempo de execução** e **espaço de memória** utilizado. O objetivo é otimizar o uso desses recursos e escolher as soluções mais eficientes para problemas computacionais.

### **Por que Analisar Algoritmos?**

* **Economia de Recursos:** Algoritmos eficientes economizam tempo de processamento e memória, o que resulta em redução de custos operacionais.
* **Escalabilidade:** Permite entender como o desempenho de um algoritmo é afetado pelo aumento do tamanho da entrada de dados.
* **Comparação Objetiva:** Fornece métricas claras e matemáticas para comparar diferentes algoritmos que resolvem o mesmo problema.

### **Notações Assintóticas: Medindo a Eficiência**

As notações assintóticas descrevem o comportamento de um algoritmo conforme a entrada tende ao infinito. Elas nos ajudam a entender os limites de desempenho.

| Notação            | Representa  | Descrição                                                                                                                                                                |
| :------------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **O (Big-O)**  | Pior Caso   | Estabelece um **limite superior** para o crescimento da função. É a notação mais comum, pois garante que o desempenho do algoritmo não será pior que este limite. |
| **Ω (Omega)** | Melhor Caso | Estabelece um **limite inferior**. O algoritmo não será mais rápido que este limite.                                                                                  |
| **Θ (Theta)** | Caso Médio | Estabelece **ambos os limites**, superior e inferior, descrevendo o comportamento médio e mais preciso do algoritmo.                                                    |

### **Paradigmas de Projeto de Algoritmos**

Paradigmas são estratégias ou abordagens gerais para construir soluções eficientes.

* **Divisão e Conquista:**

  * **Estratégia:** Divide o problema em subproblemas menores, resolve cada um de forma independente e depois combina as soluções.
  * **Exemplos:** MergeSort, QuickSort.
* **Algoritmos Gulosos (Greedy):**

  * **Estratégia:** Toma a decisão localmente ótima em cada passo, na esperança de encontrar a solução globalmente ótima. É uma abordagem que nem sempre garante a melhor resposta, mas é frequentemente rápida.
  * **Exemplos:** Problema da Mochila Fracionária, Algoritmo de Dijkstra.
* **Programação Dinâmica:**

  * **Estratégia:** Resolve subproblemas sobrepostos uma única vez e armazena seus resultados em uma tabela (memoização) para evitar recálculos.
  * **Exemplos:** Sequência de Fibonacci otimizada, Problema da Mochila 0/1.
* **Branch and Bound:**

  * **Estratégia:** Explora uma árvore de soluções de forma sistemática. Em cada passo, "poda" ramos inteiros da árvore que não levarão a uma solução ótima, reduzindo o espaço de busca.
  * **Exemplos:** Problema do Caixeiro Viajante, Alocação de Tarefas.

---

## ⚙️ **Parte 2: Teoria dos Autômatos e Computabilidade**

Esta área estuda os modelos matemáticos da computação para definir os limites do que é computável. É a base para compiladores, processamento de linguagem natural e verificação de sistemas.

### **Autômatos Finitos e Linguagens Regulares**

* **Autômato Finito Determinístico (AFD):** Um modelo simples com um número finito de estados. Para cada estado e símbolo de entrada, existe apenas uma transição possível. Não possui memória além do estado em que se encontra.
* **Autômato Finito Não-Determinístico (AFN):** Mais flexível que o AFD, permite múltiplas transições para um mesmo símbolo e transições "vazias" (ε), sem consumir um símbolo da entrada.

> **💡 Ponto Chave: O Teorema de Kleene**
> Este teorema fundamental afirma que Autômatos Finitos (AFD e AFN), Expressões Regulares e Linguagens Regulares são equivalentes em poder computacional. Qualquer linguagem que pode ser descrita por um desses modelos, pode ser descrita pelos outros dois.

### **Linguagens Não Regulares**

São linguagens que **não podem** ser reconhecidas por autômatos finitos.

> **Por que existem?**
> Autômatos finitos não possuem memória para contar ou comparar trechos de uma entrada. Se uma linguagem exige essa capacidade (ex: a linguagem de todas as strings com `n` zeros seguidos por `n` uns), ela não é regular.

### **A Hierarquia de Chomsky**

Classifica as linguagens formais em níveis de complexidade crescente.

* **Tipo 3: Linguagens Regulares:** Reconhecidas por Autômatos Finitos.
* **Tipo 2: Linguagens Livres de Contexto:** Reconhecidas por Autômatos com Pilha.
* **Tipo 1: Linguagens Sensíveis ao Contexto:** Reconhecidas por Autômatos Linearmente Limitados.
* **Tipo 0: Linguagens Recursivamente Enumeráveis:** Reconhecidas por Máquinas de Turing.

### **Máquinas de Turing: O Limite da Computação**

É o modelo computacional mais poderoso, proposto por Alan Turing. Ela pode simular qualquer algoritmo executável.

* **Componentes Principais:**
  * **Fita Infinita:** Atua como a memória ilimitada da máquina.
  * **Cabeçote:** Lê e escreve símbolos na fita, movendo-se para esquerda ou direita.
  * **Unidade de Controle:** Um conjunto finito de estados que dita as ações da máquina com base no estado atual e no símbolo lido.

> **💻 A Máquina de Turing Universal**
> É uma Máquina de Turing especial que pode simular **qualquer outra** Máquina de Turing. Este é o conceito teórico que fundamenta os computadores de propósito geral que usamos hoje: um único hardware que pode executar qualquer software (programa) que fornecemos como dado.

### **Decidibilidade: O que é Possível Resolver?**

* **Problemas Decidíveis:** Existe um algoritmo (uma Máquina de Turing) que sempre para e retorna uma resposta definitiva "sim" ou "não".
* **Problemas Indecidíveis:** **Não existe** um algoritmo que possa resolver todas as instâncias do problema.
  * **Exemplo Clássico: O Problema da Parada.** É impossível criar um programa que possa analisar qualquer outro programa e determinar, com 100% de certeza, se ele vai parar (terminar) ou entrar em loop infinito.

---
