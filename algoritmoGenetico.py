import random

# Parâmetros do algoritmo

TAMANHO_POPULACAO = 10
TAMANHO_GENOMA = 30
GERACOES = 50
TAXA_MUTACAO = 0.01

# Passo 1: Inicializar a população

def inicializar_populacao():
    return [[random.randint(0, 1) for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_POPULACAO)]

# Passo 2: Avaliar a aptidão de cada indivíduo

def avaliar_fitness(individuo):
    return sum(individuo)

# Passo 3: Seleção de pais (Torneio) | (Roleta)

def selecionar_pais(populacao, fitness):
    tamanho_torneio = 3
    pai1 = max(random.sample(list(zip(populacao, fitness)), tamanho_torneio), key=lambda x: x[1])[0]
    pai2 = max(random.sample(list(zip(populacao, fitness)), tamanho_torneio), key=lambda x: x[1])[0]

    return pai1, pai2

def selecionar_pais_roleta(populacao, fitness):
    # Calcular aptidão total
    total_fitness = sum(fitness)
    probabilidades = [f / total_fitness for f in fitness]

    # Escolher pais com base nas probabilidades
    pai1 = random.choices(populacao, weights=probabilidades, k=1)[0]
    pai2 = random.choices(populacao, weights=probabilidades, k=1)[0]

    return pai1, pai2

# Passo 4: Cruzamento (recombinação)

def crossover(pai1, pai2):
    ponto_cruzamento = random.randint(1, TAMANHO_GENOMA - 1)
    filho1 = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
    filho2 = pai2[:ponto_cruzamento] + pai1[ponto_cruzamento:]

    return filho1, filho2

# Passo 5: Mutação

def mutar(individuo):
    for i in range(TAMANHO_GENOMA):
        if(random.random() < TAXA_MUTACAO):
            individuo[i] = 1 - individuo[i] # Alterna entre 0 e 1
    
    return individuo
    
# Algoritmo Genético
    
def algoritmo_genetico():
    populacao = inicializar_populacao()

    for geracao in range(GERACOES):
        # Avaliar a aptidão de cada indivíduo
        fitness = [avaliar_fitness(individuo) for individuo in populacao]

        # Exibir o melhor indivíduo da geração
        melhor_individuo = max(populacao, key=avaliar_fitness)
        print(f"Geração {geracao}: Melhor aptidão = {avaliar_fitness(melhor_individuo)} | Melhor indivíduo = {melhor_individuo}")

        nova_populacao = []

        # Criar nova geração com cruzamento e mutação
        while(len(nova_populacao) < TAMANHO_POPULACAO):
            pai1, pai2 = selecionar_pais(populacao, fitness)

            filho1, filho2 = crossover(pai1, pai2)

            nova_populacao.append(mutar(filho1))
            nova_populacao.append(mutar(filho2))

        populacao = nova_populacao

    return max(populacao, key=avaliar_fitness)

# Executar o algoritmo

melhor_solucao = algoritmo_genetico()
print("\nMelhor solução encontrada:")
print(f"Genes: {melhor_solucao}")
print(f"Fitness: {avaliar_fitness(melhor_solucao)}")