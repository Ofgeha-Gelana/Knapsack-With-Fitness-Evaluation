import random

def fitness(individual, weight_limit, items):
    total_weight = sum(items[i]["Weight"] for i in range(len(individual)) if individual[i] == 1)
    total_value = sum(items[i]["Value"] for i in range(len(individual)) if individual[i] == 1)
    return total_value if total_weight <= weight_limit else 0

def initialize_population(pop_size, n):
    return [random_individual(n) for _ in range(pop_size)]

def random_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

def select_top_individuals(population, k, weight_limit, items):
    return sorted(population, key=lambda ind: fitness(ind, weight_limit, items), reverse=True)[:k]

def learn_distribution(top_individuals, n):
    probabilities = [0.0] * n
    for i in range(n):
        ones_count = sum(ind[i] for ind in top_individuals)
        probabilities[i] = ones_count / len(top_individuals)
    return probabilities

def sample_new_individual(probabilities):
    return [1 if random.random() < p else 0 for p in probabilities]
