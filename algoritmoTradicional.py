import random

# Parâmetros do algoritmo

QUANT_CIDADES = 5
CIDADE_ORIGEM = 0

TAMANHO_POPULACAO = 10
TAMANHO_GENOMA = QUANT_CIDADES + 1
GERACOES = 10
TAXA_MUTACAO = 0.05

def gerarMatrizCaminhos():
    matrizCaminhos = [[0 for _ in range(QUANT_CIDADES)] for _ in range(QUANT_CIDADES)]

    for i in range(QUANT_CIDADES):
        for j in range(QUANT_CIDADES):
            if(i != j):
                peso = random.randint(1, 20)

                adicionarCaminho(matrizCaminhos, i, j, peso)

    return matrizCaminhos

def adicionarCaminho(matrizCaminhos, origem, destino, peso):
    matrizCaminhos[origem][destino] = peso
    matrizCaminhos[destino][origem] = peso

# Inicialização da matriz de adjacência dos caminhos entre as cidades

matrizCaminhos = [[0 for _ in range(QUANT_CIDADES)] for _ in range(QUANT_CIDADES)]

adicionarCaminho(matrizCaminhos, 0, 1, 15)
adicionarCaminho(matrizCaminhos, 0, 2, 12)
adicionarCaminho(matrizCaminhos, 0, 3, 7)
adicionarCaminho(matrizCaminhos, 0, 4, 4)
adicionarCaminho(matrizCaminhos, 1, 2, 10)
adicionarCaminho(matrizCaminhos, 1, 3, 20)
adicionarCaminho(matrizCaminhos, 1, 4, 14)
adicionarCaminho(matrizCaminhos, 2, 3, 9)
adicionarCaminho(matrizCaminhos, 2, 4, 8)
adicionarCaminho(matrizCaminhos, 3, 4, 16)

for i in range(len(matrizCaminhos)):
    print(matrizCaminhos[i])

# Inicialização da população

def inicializarPopulacao():
    populacao = [[-1 for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_POPULACAO)]

    for i in range(TAMANHO_POPULACAO):
        for j in range(TAMANHO_GENOMA):
            if(j == 0 or j == TAMANHO_GENOMA - 1):
                populacao[i][j] = CIDADE_ORIGEM
            else:
                while(populacao[i][j] == -1):
                    destino = random.randint(0, QUANT_CIDADES - 1)

                    if(destino not in populacao[i]):
                        populacao[i][j] = destino

    return populacao

def avaliarFitness(individuo):
    fitness = 0
    
    for i in range(QUANT_CIDADES):
        origem = individuo[i]
        destino = individuo[i + 1]

        fitness += matrizCaminhos[origem][destino]

    return fitness

def selecionarPais(populacao, fitness):
    tamanhoTorneio = 3

    amostra = random.sample(list(zip(populacao, fitness)), tamanhoTorneio)

    pai1 = min(amostra, key=lambda x: x[1])[0]

    for i in range(len(amostra)):
        if(amostra[i][0] == pai1):
            posicao = i

    amostra.pop(posicao)

    pai2 = min(amostra, key=lambda x: x[1])[0]

    return pai1, pai2

# Cruzamento parcialmente mapeado

def crossover(pai1, pai2):
    ponto1 = random.randint(2, TAMANHO_GENOMA - 3) # Começa em 2 para evitar um ponto ao lado da cidade de origem; e termina em TAMANHO_GENOMA - 3 para evitar a mesma coisa e para ter pelo menos um gene (!= origem) depois do 2º ponto
    ponto2 = random.randint(ponto1 + 1, TAMANHO_GENOMA - 2) # Começa logo depois do 1º ponto para ter pelo menos um gene entre os dois pontos; e termina em TAMANHO_GENOMA - 2 para evitar um ponto ao lado da cidade de origem e para ter pelo menos um gene (!= origem) depois do 2º ponto

    filho1 = [-1 for _ in range(TAMANHO_GENOMA)]
    filho2 = [-1 for _ in range(TAMANHO_GENOMA)]

    filho1[ponto1:ponto2] = pai2[ponto1:ponto2]
    filho2[ponto1:ponto2] = pai1[ponto1:ponto2]

    # print("Parte 1:")
    # print(f"Ponto de cruzamento 1: {ponto1}; e Ponto de cruzamento 2: {ponto2}")
    # print(f"Pai 1: {pai1}; e Pai 2: {pai2}")
    # print(f"Filho 1: {filho1}; e Filho 2: {filho2}\n")

    restantePai1 = []
    restantePai2 = []

    for i in range(TAMANHO_GENOMA):
        if(i == 0 or i == TAMANHO_GENOMA - 1):
            filho1[i] = filho2[i] = CIDADE_ORIGEM
        else:
            if(filho1[i] == -1):
                if(pai1[i] not in filho1):
                    filho1[i] = pai1[i]
                else:
                    restantePai1.insert(0, pai1[i])

            if(filho2[i] == -1):
                if(pai2[i] not in filho2):
                    filho2[i] = pai2[i]
                else:
                    restantePai2.insert(0, pai2[i])

    # print("Parte 2:")
    # print(f"Filho 1: {filho1}; e Filho 2: {filho2}\n")

    if(-1 in filho1 or -1 in filho2):
        for i in range(TAMANHO_GENOMA):
            if(filho1[i] == -1):
                filho1[i] = restantePai2.pop()
            
            if(filho2[i] == -1):
                filho2[i] = restantePai1.pop()

    # print("Parte 3:")
    # print(f"Filho 1: {filho1}; e Filho 2: {filho2}\n")  

    return filho1, filho2

def fazerMutacao(individuo):
    # print(f"Indivíduo: {individuo}")

    for i in range(TAMANHO_GENOMA):
        if(i > 0 and i < TAMANHO_GENOMA - 1):
            if(random.random() < TAXA_MUTACAO):
                segundoGene = i

                while(segundoGene == i):
                    segundoGene = random.randint(1, TAMANHO_GENOMA - 2)

                aux = individuo[i]
                individuo[i] = individuo[segundoGene]
                individuo[segundoGene] = aux

    # print(f"Indivíduo com mutação: {individuo}\n")

    return individuo

# Algoritmo Genético

def executarAG():
    populacao = inicializarPopulacao()

    print(populacao)

    for geracao in range(GERACOES):
        fitness = [avaliarFitness(individuo) for individuo in populacao]

        melhorIndividuo = min(populacao, key=avaliarFitness)
        print(f"Geração {geracao}: Melhor aptidão = {avaliarFitness(melhorIndividuo)} | Melhor indivíduo = {melhorIndividuo}")
        
        novaPopulacao = []

        while(len(novaPopulacao) < TAMANHO_POPULACAO):
            pai1, pai2 = selecionarPais(populacao, fitness)

            filho1, filho2 = crossover(pai1, pai2)
            # print(f"Filho 1: {filho1}; e Filho 2: {filho2}")

            novaPopulacao.append(fazerMutacao(filho1))
            novaPopulacao.append(fazerMutacao(filho2))

        populacao = novaPopulacao

    return min(populacao, key=avaliarFitness)

melhorSolucao = executarAG()
print("\nMelhor solução encontrada:")
print(f"Rota: {melhorSolucao}")
print(f"Fitness: {avaliarFitness(melhorSolucao)}")