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

adicionarCaminho(0, 1, 3)

for i in range(len(matrizCaminhos)):
    print(matrizCaminhos[i])

populacao = [[]]

print(populacao)

# Inicialização da população

def inicializarPopulacao():
    populacao = [[]]

    for i in range(TAMANHO_POPULACAO):
        for j in range(QUANT_CIDADES + 1):
            if(j == 0 or j == QUANT_CIDADES + 1):
                populacao[i][j] = CIDADE_ORIGEM
            else:
                cidadeAnterior = populacao[i][j - 1]

                destino = random.randint(0, QUANT_CIDADES - 1)

                if(matrizCaminhos[cidadeAnterior][destino] > 0):
                    populacao[i][j] = destino
            
