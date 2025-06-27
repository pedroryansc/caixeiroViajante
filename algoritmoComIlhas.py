import math, random

# Parâmetros do algoritmo

QUANT_CIDADES = 5
CIDADE_ORIGEM = 0

TAMANHO_POPULACAO = 30
TAMANHO_GENOMA = QUANT_CIDADES + 1
GERACOES = 10
TAXA_MUTACAO = 0.01

# Parâmetros da estratégia com ilhas

QUANT_ILHAS = 3
TAMANHO_ILHA = math.ceil(TAMANHO_POPULACAO / QUANT_ILHAS)
FREQ_MIGRACAO = 3
TAXA_MIGRACAO = 2

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

matrizCaminhos = gerarMatrizCaminhos() # [[0 for _ in range(QUANT_CIDADES)] for _ in range(QUANT_CIDADES)]
'''
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
'''

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
                # não está rota é adicionada
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
        migracao = random.sample(ilha, TAXA_MIGRACAO)

        # Os indivíduos escolhidos são removidos da subpopulação de sua ilha 
        for i in range(TAXA_MIGRACAO):
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

    return min(solucoesIlhas, key=avaliarFitness)

# Execução do algoritmo

melhorSolucao = executarAG()
print("\nMelhor solução encontrada:")
print(f"Rota: {melhorSolucao}")
print(f"Fitness: {avaliarFitness(melhorSolucao)}")