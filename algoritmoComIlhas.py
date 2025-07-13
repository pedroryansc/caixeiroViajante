import math, random

# Parâmetros do algoritmo

QUANT_CIDADES = 30
CIDADE_ORIGEM = 0

TAMANHO_POPULACAO = 30
TAMANHO_GENOMA = QUANT_CIDADES + 1
GERACOES = 100
TAXA_MUTACAO = 0.01

# Parâmetros da estratégia com ilhas

QUANT_ILHAS = 3
TAMANHO_ILHA = math.ceil(TAMANHO_POPULACAO / QUANT_ILHAS)
FREQ_MIGRACAO = 3
TAXA_MIGRACAO = 0.2
QUANT_MIGRACAO = math.ceil(TAMANHO_ILHA * TAXA_MIGRACAO)

# Função para criar a matriz dos caminhos entre as cidades com distâncias definidas aleatoriamente

def gerarMatrizCaminhos():
    matrizCaminhos = [[0 for _ in range(QUANT_CIDADES)] for _ in range(QUANT_CIDADES)]

    for i in range(QUANT_CIDADES):
        for j in range(QUANT_CIDADES):
            if(i != j):
                peso = random.randint(1, 20)

                adicionarCaminho(matrizCaminhos, i, j, peso)

    return matrizCaminhos

# Função que adiciona um caminho não direcionado entre duas cidades

def adicionarCaminho(matrizCaminhos, origem, destino, peso):
    matrizCaminhos[origem][destino] = peso
    matrizCaminhos[destino][origem] = peso

# Inicialização da matriz dos caminhos entre as cidades

matrizCaminhos = matrizCaminhos = [ # gerarMatrizCaminhos()
    [0, 4, 10, 20, 18, 10, 7, 9, 12, 2, 9, 3, 1, 18, 14, 14, 12, 10, 3, 18, 16, 19, 15, 20, 14, 5, 9, 10, 17, 17],
    [4, 0, 19, 13, 12, 1, 17, 13, 3, 2, 12, 4, 6, 3, 4, 17, 9, 20, 6, 4, 9, 19, 19, 20, 2, 9, 15, 14, 20, 9],
    [10, 19, 0, 1, 2, 9, 15, 7, 8, 16, 13, 11, 6, 20, 7, 1, 9, 5, 1, 19, 6, 12, 5, 4, 5, 15, 13, 12, 13, 8],
    [20, 13, 1, 0, 12, 1, 15, 4, 11, 14, 9, 19, 1, 2, 10, 12, 14, 9, 2, 18, 8, 6, 2, 6, 1, 6, 12, 17, 4, 10],
    [18, 12, 2, 12, 0, 17, 16, 18, 19, 1, 2, 4, 1, 9, 14, 15, 12, 12, 19, 16, 19, 8, 20, 6, 16, 20, 9, 10, 3, 11],
    [10, 1, 9, 1, 17, 0, 2, 12, 14, 8, 13, 15, 1, 3, 2, 2, 10, 1, 4, 19, 20, 15, 11, 12, 10, 16, 6, 18, 5, 5],
    [7, 17, 15, 15, 16, 2, 0, 1, 3, 10, 18, 10, 4, 17, 16, 1, 5, 15, 17, 1, 6, 8, 4, 19, 20, 11, 1, 1, 4, 2],
    [9, 13, 7, 4, 18, 12, 1, 0, 9, 10, 16, 1, 11, 20, 16, 6, 10, 10, 18, 1, 5, 11, 4, 17, 1, 7, 8, 6, 11, 7],
    [12, 3, 8, 11, 19, 14, 3, 9, 0, 8, 1, 11, 9, 14, 16, 5, 5, 15, 18, 2, 3, 16, 6, 4, 5, 20, 11, 2, 14, 17],
    [2, 2, 16, 14, 1, 8, 10, 10, 8, 0, 20, 7, 7, 8, 10, 12, 14, 20, 16, 18, 13, 20, 1, 12, 8, 16, 14, 7, 7, 5],
    [9, 12, 13, 9, 2, 13, 18, 16, 1, 20, 0, 13, 20, 14, 4, 6, 1, 19, 15, 15, 18, 8, 2, 6, 8, 18, 3, 11, 5, 17],
    [3, 4, 11, 19, 4, 15, 10, 1, 11, 7, 13, 0, 9, 4, 13, 15, 7, 10, 13, 5, 1, 3, 7, 16, 9, 5, 12, 3, 5, 4],
    [1, 6, 6, 1, 1, 1, 4, 11, 9, 7, 20, 9, 0, 5, 17, 19, 14, 1, 12, 9, 20, 13, 2, 15, 19, 19, 10, 5, 11, 6],
    [18, 3, 20, 2, 9, 3, 17, 20, 14, 8, 14, 4, 5, 0, 15, 11, 10, 6, 2, 11, 20, 7, 4, 9, 9, 11, 2, 3, 16, 18],
    [14, 4, 7, 10, 14, 2, 16, 16, 16, 10, 4, 13, 17, 15, 0, 10, 5, 4, 15, 1, 20, 14, 16, 9, 15, 5, 16, 8, 18, 19],
    [14, 17, 1, 12, 15, 2, 1, 6, 5, 12, 6, 15, 19, 11, 10, 0, 3, 12, 16, 5, 3, 7, 19, 11, 3, 1, 12, 13, 2, 11],
    [12, 9, 9, 14, 12, 10, 5, 10, 5, 14, 1, 7, 14, 10, 5, 3, 0, 2, 1, 17, 10, 17, 5, 3, 8, 6, 19, 9, 17, 15],
    [10, 20, 5, 9, 12, 1, 15, 10, 15, 20, 19, 10, 1, 6, 4, 12, 2, 0, 14, 14, 4, 8, 11, 16, 15, 2, 7, 15, 5, 1],
    [3, 6, 1, 2, 19, 4, 17, 18, 18, 16, 15, 13, 12, 2, 15, 16, 1, 14, 0, 6, 20, 1, 3, 1, 7, 18, 1, 3, 8, 2],
    [18, 4, 19, 18, 16, 19, 1, 1, 2, 18, 15, 5, 9, 11, 1, 5, 17, 14, 6, 0, 7, 4, 5, 19, 8, 11, 2, 11, 12, 15],
    [16, 9, 6, 8, 19, 20, 6, 5, 3, 13, 18, 1, 20, 20, 20, 3, 10, 4, 20, 7, 0, 7, 8, 2, 2, 14, 11, 15, 13, 5],
    [19, 19, 12, 6, 8, 15, 8, 11, 16, 20, 8, 3, 13, 7, 14, 7, 17, 8, 1, 4, 7, 0, 15, 15, 11, 5, 19, 8, 7, 2],
    [15, 19, 5, 2, 20, 11, 4, 4, 6, 1, 2, 7, 2, 4, 16, 19, 5, 11, 3, 5, 8, 15, 0, 5, 14, 19, 15, 10, 17, 20],
    [20, 20, 4, 6, 6, 12, 19, 17, 4, 12, 6, 16, 15, 9, 9, 11, 3, 16, 1, 19, 2, 15, 5, 0, 6, 18, 16, 1, 12, 3],
    [14, 2, 5, 1, 16, 10, 20, 1, 5, 8, 8, 9, 19, 9, 15, 3, 8, 15, 7, 8, 2, 11, 14, 6, 0, 9, 6, 20, 15, 9],
    [5, 9, 15, 6, 20, 16, 11, 7, 20, 16, 18, 5, 19, 11, 5, 1, 6, 2, 18, 11, 14, 5, 19, 18, 9, 0, 3, 16, 17, 2],
    [9, 15, 13, 12, 9, 6, 1, 8, 11, 14, 3, 12, 10, 2, 16, 12, 19, 7, 1, 2, 11, 19, 15, 16, 6, 3, 0, 11, 9, 8],
    [10, 14, 12, 17, 10, 18, 1, 6, 2, 7, 11, 3, 5, 3, 8, 13, 9, 15, 3, 11, 15, 8, 10, 1, 20, 16, 11, 0, 4, 4],
    [17, 20, 13, 4, 3, 5, 4, 11, 14, 7, 5, 5, 11, 16, 18, 2, 17, 5, 8, 12, 13, 7, 17, 12, 15, 17, 9, 4, 0, 6],
    [17, 9, 8, 10, 11, 5, 2, 7, 17, 5, 17, 4, 6, 18, 19, 11, 15, 1, 2, 15, 5, 2, 20, 3, 9, 2, 8, 4, 6, 0]
]

for i in range(len(matrizCaminhos)):
    print(matrizCaminhos[i])

# Passo 1: Inicialização da população

def inicializarPopulacao():
    # A população é dividida em ilhas, as quais têm a mesma quantidade de indivíduos
    populacao = [[[-1 for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_ILHA)] for _ in range(QUANT_ILHAS)]

    for ilha in populacao:
        for i in range(TAMANHO_ILHA):
            for j in range(TAMANHO_GENOMA):
                # Verificação para adicionar a cidade de origem no início e fim da rota
                if(j == 0 or j == TAMANHO_GENOMA - 1):
                    ilha[i][j] = CIDADE_ORIGEM
                # Caso seja outra posição do cromossomo, uma cidade aleatória que ainda 
                # não está na rota é adicionada
                else:
                    while(ilha[i][j] == -1):
                        destino = random.randint(0, QUANT_CIDADES - 1)

                        if(destino not in ilha[i]):
                            ilha[i][j] = destino

    return populacao

# Passo 2: Avaliação do fitness/aptidão de cada indivíduo

def avaliarFitness(individuo):
    # A partir da matriz que contém a distância (peso) dos caminhos, a função de fitness
    # soma a distância total da rota
    fitness = 0
    
    for i in range(QUANT_CIDADES):
        origem = individuo[i]
        destino = individuo[i + 1]

        fitness += matrizCaminhos[origem][destino]

    return fitness

# Passo 3: Seleção de pais (Torneio)

def selecionarPais(populacao, fitness):
    tamanhoTorneio = 3

    # Uma quantidade de indivíduos da população é selecionada
    amostra = random.sample(list(zip(populacao, fitness)), tamanhoTorneio)

    # O indivíduo com a menor pontuação da amostra é escolhido como o primeiro pai
    pai1 = min(amostra, key=lambda x: x[1])[0]

    # Para evitar a possibilidade do mesmo indivíduo ser selecionado como o segundo pai,
    # o primeiro pai é removido da amostra
    for i in range(tamanhoTorneio):
        if(amostra[i][0] == pai1):
            posicao = i

    amostra.pop(posicao)

    # O indivíduo com a atual menor pontuação da amostra se torna o segundo pai
    pai2 = min(amostra, key=lambda x: x[1])[0]

    return pai1, pai2

# Passo 4: Cruzamento (Parcialmente Mapeado)

def crossover(pai1, pai2):
    # Dois pontos de corte são definidos aleatoriamente:
    
    # Intervalo para escolher o Ponto 1:
    # Começo: 2 -> Evita um ponto de corte ao lado da cidade de origem;
    # Fim: "TAMANHO_GENOMA - 3" -> Evita a mesma coisa e garante pelo menos um gene (além da origem) depois do Ponto 2
    ponto1 = random.randint(2, TAMANHO_GENOMA - 3)

    # Intervalo para escolher o Ponto 2:
    # Começo: Logo após o Ponto 1 -> Garante pelo menos um gene entre os dois pontos;
    # Fim: "TAMANHO_GENOMA - 2" -> Evita um ponto ao lado da cidade de origem e garante pelo menos um gene (além da origem) depois do Ponto 2
    ponto2 = random.randint(ponto1 + 1, TAMANHO_GENOMA - 2)

    filho1 = [-1 for _ in range(TAMANHO_GENOMA)]
    filho2 = [-1 for _ in range(TAMANHO_GENOMA)]

    # Filho 1 recebe a parte intermediária (delimitada pelos pontos de corte) do Pai 2
    filho1[ponto1:ponto2] = pai2[ponto1:ponto2]

    # Filho 2 recebe a parte intermediária do Pai 1
    filho2[ponto1:ponto2] = pai1[ponto1:ponto2]

    restantePai1 = []
    restantePai2 = []

    # Os filhos recebem os genes das partes esquerda e direita dos pais
    # (com exceção dos genes que já se encontram nos descendentes)
    for i in range(TAMANHO_GENOMA):
        # Adicionando as cidades de origem nos descendentes
        if(i == 0 or i == TAMANHO_GENOMA - 1):
            filho1[i] = filho2[i] = CIDADE_ORIGEM
        else:
            if(filho1[i] == -1):
                # Se o gene do Pai 1 não está no Filho 1, esse gene é adicionado 
                # na mesma posição no cromossomo do filho
                if(pai1[i] not in filho1):
                    filho1[i] = pai1[i]
                # Caso contrário, o gene é inserido na lista dos genes do Pai 1 
                # que ainda não foram usados
                else:
                    restantePai1.insert(0, pai1[i])

            if(filho2[i] == -1):
                # Se o gene do Pai 2 não está no Filho 2, esse gene é adicionado 
                # na mesma posição no cromossomo do filho
                if(pai2[i] not in filho2):
                    filho2[i] = pai2[i]
                # Caso contrário, o gene é inserido na lista dos genes do Pai 2 
                # que ainda não foram usados
                else:
                    restantePai2.insert(0, pai2[i])

    # Os campos vazios do Filho 1 são preenchidos com os valores do Pai 2;
    # E os campos vazios do Filho 2 são preenchidos com os do Pai 1
    if(-1 in filho1 or -1 in filho2):
        for i in range(TAMANHO_GENOMA):
            if(filho1[i] == -1):
                filho1[i] = restantePai2.pop()
            
            if(filho2[i] == -1):
                filho2[i] = restantePai1.pop()

    return filho1, filho2

# Passo 5: Mutação (Troca)

def fazerMutacao(individuo):
    for i in range(TAMANHO_GENOMA):
        if(i > 0 and i < TAMANHO_GENOMA - 1):
            # Verificação para decidir se o gene será trocado de posição com
            # outro gene escolhido aleatoriamente
            if(random.random() < TAXA_MUTACAO):
                segundoGene = i

                # Loop para garantir que o segundo gene da troca não seja o
                # mesmo que o primeiro
                while(segundoGene == i):
                    segundoGene = random.randint(1, TAMANHO_GENOMA - 2)

                aux = individuo[i]
                individuo[i] = individuo[segundoGene]
                individuo[segundoGene] = aux

    return individuo

# Migração de indivíduos (Topologia em anel)

def migrarIndividuos(populacao):
    individuosMigracao = []

    # Escolha aleatória dos indivíduos que vão migrar para outras ilhas
    for ilha in populacao:
        migracao = random.sample(ilha, QUANT_MIGRACAO)

        # Os indivíduos escolhidos são removidos da subpopulação de sua ilha 
        for i in range(QUANT_MIGRACAO):
            for posicaoIndividuo in range(len(ilha)):
                if(ilha[posicaoIndividuo] == migracao[i]):
                    posicao = posicaoIndividuo

            ilha.pop(posicao)

        individuosMigracao.append(migracao)

    # Migração dos indivíduos para a ilha seguinte na topologia em anel
    for ilha in range(QUANT_ILHAS):
        # Caso seja a primeira ilha, ela receberá os indivíduos da última ilha
        # (a qual é anterior à ela)
        if(ilha == 0):
            for individuo in individuosMigracao[QUANT_ILHAS - 1]:
                populacao[ilha].append(individuo)
        # Caso contrário, a ilha recebe os indivíduos da ilha anterior normalmente
        else:
            for individuo in individuosMigracao[ilha - 1]:
                populacao[ilha].append(individuo)

    return populacao

# Algoritmo Genético

def executarAG():
    populacao = inicializarPopulacao()

    for ilha in range(QUANT_ILHAS):
        print(f"Ilha {ilha}: {populacao[ilha]}")

    geracoesMigracao = 0

    for geracao in range(GERACOES):
        print(f"\nGeração {geracao}:")

        geracoesMigracao += 1

        # Em cada geração, cada ilha tem sua subpopulação atualizada
        for ilha in range(QUANT_ILHAS):
            # Avaliação da aptidão de cada indivíduo
            fitness = [avaliarFitness(individuo) for individuo in populacao[ilha]]

            melhorIndividuo = min(populacao[ilha], key=avaliarFitness)
            print(f"Ilha {ilha}: Melhor aptidão = {avaliarFitness(melhorIndividuo)} | Melhor indivíduo = {melhorIndividuo}")
            
            novaIlha = []

            # Criação da nova geração
            while(len(novaIlha) < TAMANHO_ILHA):
                pai1, pai2 = selecionarPais(populacao[ilha], fitness)

                filho1, filho2 = crossover(pai1, pai2)

                novaIlha.append(fazerMutacao(filho1))
                novaIlha.append(fazerMutacao(filho2))

            populacao[ilha] = novaIlha
        
        # Se a frequência de migração é atingida, a migração de indivíduos é realizada
        if(geracoesMigracao == FREQ_MIGRACAO):
            populacao = migrarIndividuos(populacao)

            geracoesMigracao = 0

    solucoesIlhas = []

    # Apresentação da melhor solução encontrada em cada ilha
    for ilha in range(QUANT_ILHAS):
        melhorSolucaoIlha = min(populacao[ilha], key=avaliarFitness)

        print(f"\nMelhor solução da Ilha {ilha}: {melhorSolucaoIlha} - Fitness de {avaliarFitness(melhorSolucaoIlha)}")

        solucoesIlhas.append(melhorSolucaoIlha)

    # O resultado do AG é a melhor solução entre todas as ilhas, ou seja, a que apresenta o caminho mais curto
    return min(solucoesIlhas, key=avaliarFitness)

# Execução do algoritmo

import time

inicio = time.time()
melhorSolucao = executarAG()
fim = time.time()

tempo = fim - inicio

print("\nMelhor solução encontrada:")
print(f"Rota: {melhorSolucao}")
print(f"Fitness: {avaliarFitness(melhorSolucao)}")
print(f"Tempo de execução (s): {tempo}")