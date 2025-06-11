import random

# Parâmetros do algoritmo

TAMANHO_POPULACAO = 10
QUANT_CIDADES = 5
CIDADE_ORIGEM = 0
GERACOES = 50
TAXA_MUTACAO = 0.01

# Inicialização da matriz de adjacência dos caminhos entre as cidades

def adicionarCaminho(origem, destino, peso):
    matrizCaminhos[origem][destino] = peso
    matrizCaminhos[destino][origem] = peso

matrizCaminhos = [[0 for _ in range(QUANT_CIDADES)] for _ in range(QUANT_CIDADES)]

adicionarCaminho(0, 1, 15)
adicionarCaminho(0, 2, 12)
adicionarCaminho(0, 3, 7)
adicionarCaminho(0, 4, 4)
adicionarCaminho(1, 2, 10)
adicionarCaminho(1, 3, 20)
adicionarCaminho(1, 4, 14)
adicionarCaminho(2, 3, 9)
adicionarCaminho(2, 4, 8)
adicionarCaminho(3, 4, 16)

for i in range(len(matrizCaminhos)):
    print(matrizCaminhos[i])

# Inicialização da população

def inicializarPopulacao():
    populacao = [[-1 for _ in range(QUANT_CIDADES + 1)] for _ in range(TAMANHO_POPULACAO)]

    for i in range(TAMANHO_POPULACAO):
        for j in range(QUANT_CIDADES + 1):
            if(j == 0 or j == QUANT_CIDADES):
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

    pai1 = min(random.sample(list(zip(populacao, fitness)), tamanhoTorneio), key=lambda x: x[1])[0]
    pai2 = min(random.sample(list(zip(populacao, fitness)), tamanhoTorneio), key=lambda x: x[1])[0]

    return pai1, pai2

# Algoritmo Genético

def algoritmoGenetico():
    populacao = inicializarPopulacao()

    print(populacao)

    for geracao in range(GERACOES):
        fitness = [avaliarFitness(individuo) for individuo in populacao]

        melhorIndividuo = min(populacao, key=avaliarFitness)
        print(f"Geração {geracao}: Melhor aptidão = {avaliarFitness(melhorIndividuo)} | Melhor indivíduo = {melhorIndividuo}")
        '''
        novaPopulacao = []

        while(len(novaPopulacao) < TAMANHO_POPULACAO):
            pai1, pai2 = selecionarPais(populacao, fitness)

        populacao = novaPopulacao
        '''
    return min(populacao, key=avaliarFitness)

melhorSolucao = algoritmoGenetico()
print("\nMelhor solução encontrada:")
print(f"Rota: {melhorSolucao}")
print(f"Fitness: {avaliarFitness(melhorSolucao)}")