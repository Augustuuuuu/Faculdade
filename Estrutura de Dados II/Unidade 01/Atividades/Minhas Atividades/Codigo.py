""" 
// Versão01: Medir a maior e menor idade, e calcular a média das idades dos alunos
// Versão02: As medidas de tendencia central Moda e Mediana.
// Versão03: Solicitar ao usuário, alem das idades:
// O nome do aluno
// Sexo (M/F)
// As tres notas do aluno
// Ao final apresentar:
// Percentual de Alunos e Alunas aprovadas e reprovadas
// Percentual de Alunos aprovados/reprovados com mais de 20
// Relatório com os nomes e medias dos alunos aprovado e reprovados
// Configurar a média de aprovação na faculdade e quantidade de provas

// Tratar entrada de dados não permitido
// Gênero diferente de M e F (tanto faz maisc e minusc)
// Idade <16 e nem > 100 anos (não pode)
// Nota menores que zero nem maiores que dez
// ----------------------------------------------------------------------------------
"""

notas = []
aluno = {}
contador = 0
c = 0
soma = 0
somaIdade = 0
maiorIdade = 0
menorIdade = 0
maiorNome = ''
menorNome = ''
alunoAprovado20 = 0
alunoReprovado20 = 0
alunoAprovado = 0
alunoReprovado = 0
# Loop para pegar dados dos alunos
while True:
    contador += 1
    nome = input(f"Digite o nome do {contador}º aluno: ")

    # Verificando idade
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade >= 16 and idade <= 100:
                break
            else:
                print("Digite uma idade válida! Entre 16 e 100.")
        except:
            print("Digite apenas números.")
    
    somaIdade += idade

    if contador == 1:
        maiorIdade = idade
        menorIdade = idade
        menorNome = nome
        maiorNome = nome
    elif idade > maiorIdade:
        maiorIdade = idade
        maiorNome = nome
    elif idade < menorIdade:
        menorIdade = idade
        menorNome = nome
        
    # Verificando o sexo
    while True:
        sexo = input("Digite o sexo (M ou F): ").lower()
        if sexo == 'm' or 'f':
            break
        else:
            print("Digite F para feminino e M para masculino.")
    soma = 0 

    # Buscando as notas dos alunos

    for i in range(3):
        nota = float(input(f"Digite sua {i+1} nota: "))
        soma += nota
        notas.append(nota)

    if soma / 3 >= 7:
        alunoAprovado += 1
    else:
        alunoReprovado += 1

    if soma / 3 >= 7 and idade > 20:
        alunoAprovado20 += 1
        c += 1
    elif soma / 3 < 7 and idade > 20:
        alunoReprovado20 += 1
        c += 1


    aluno = {
            "Nome": nome,
            "Idade": idade,
            "Sexo": sexo,
            "Notas": notas
             }
    

    
    informar_mais = input("Deseja informar mais um aluno (S ou N)? ").lower()
    if informar_mais == 's':
        pass
    else:
        break

# Fim do Loop

print(f"A média de idades dos alunos é de {somaIdade / contador:.1f}.")
print(f"O aluno mais novo é {menorNome} com {menorIdade} anos.")
print(f"O aluno mais velho é {maiorNome} com {maiorIdade} anos.")

# Falta calcular as tendência central

print(f"Porcentagem de alunos aprovado: {alunoAprovado * 100 / contador:.0f}%")
print(f"Porcentagem de alunos reprovados: {alunoReprovado * 100 / contador:.0f}%")
print(f"Porcentagem de alunos aprovado com mais de vinte: {alunoAprovado20 * 100 / c:.0f}%")
print(f"Porcentagem de alunos reprovados com mais de vinte: {alunoReprovado20 * 100 / c:.0f}%")