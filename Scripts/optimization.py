import random
from utils import initialize_population, fitness, select_top_individuals, learn_distribution, sample_new_individual

def eda_knapsack(n, population_size, generations, top_k, weight_limit, items, progress_bar):
    population = initialize_population(population_size, n)
    best_solution = None
    best_fitness = 0
    generation_count = 0
    optimal_generation = None

    for generation in range(generations):
        generation_count += 1
        top_individuals = select_top_individuals(population, top_k, weight_limit, items)
        probabilities = learn_distribution(top_individuals, n)
        population = [sample_new_individual(probabilities) for _ in range(population_size)]
        
        current_best = max(population, key=lambda ind: fitness(ind, weight_limit, items))
        current_fitness = fitness(current_best, weight_limit, items)
        
        if current_fitness > best_fitness:
            best_solution = current_best
            best_fitness = current_fitness
            optimal_generation = generation_count
        
        progress_bar.progress((generation + 1) / generations)

        if best_fitness == sum(item["Value"] for item in items):
            break

    return best_solution, best_fitness, generation_count, optimal_generation
