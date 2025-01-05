import streamlit as st
import pandas as pd
import random
import time

# Problem Statement
st.title("Knapsack Optimization Problem")
st.markdown("""
### Problem Statement:
You are preparing for a trip and have a set of items, each with a weight and a value. The goal is to select the most valuable combination of items that fit into your bag without exceeding its weight capacity.

Use the parameters in the sidebar to adjust the weight limit and population size, and click the button to find the optimal solution.
""")

# Items Data
items = [
    {"Item": "Tent", "Weight": 5.0, "Value": 10},
    {"Item": "Sleeping Bag", "Weight": 3.5, "Value": 7},
    {"Item": "Cooking Kit", "Weight": 4.0, "Value": 8},
    {"Item": "First Aid Kit", "Weight": 1.0, "Value": 6},
    {"Item": "Water Bottle", "Weight": 2.0, "Value": 9},
    {"Item": "Clothes", "Weight": 3.0, "Value": 5},
    {"Item": "Flashlight", "Weight": 1.5, "Value": 3},
    {"Item": "Power Bank", "Weight": 1.0, "Value": 4},
    {"Item": "Snacks", "Weight": 2.5, "Value": 6},
    {"Item": "Notebook & Pen", "Weight": 0.5, "Value": 2},
]

df_items = pd.DataFrame(items)
st.markdown("### Available Items")
st.table(df_items)

# Sidebar for Parameters
st.sidebar.header("Parameters")
weight_limit = st.sidebar.slider("Weight Limit (kg)", 5.0, 20.0, 15.0, 0.5)
population_size = st.sidebar.slider("Population Size", 5, 50, 20, 1)
generations = st.sidebar.slider("Generations", 10, 100, 30, 5)
top_k = st.sidebar.slider("Top K (Selection Pool)", 1, population_size, 5, 1)

# Fitness Function
def fitness(individual):
    total_weight = sum(items[i]["Weight"] for i in range(len(individual)) if individual[i] == 1)
    total_value = sum(items[i]["Value"] for i in range(len(individual)) if individual[i] == 1)
    return total_value if total_weight <= weight_limit else 0

# Generate a Random Individual
def random_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

# Generate Initial Population
def initialize_population(pop_size, n):
    return [random_individual(n) for _ in range(pop_size)]

# Select Top K Individuals
def select_top_individuals(population, k):
    return sorted(population, key=fitness, reverse=True)[:k]

# Learn Distribution
def learn_distribution(top_individuals, n):
    probabilities = [0.0] * n
    for i in range(n):
        ones_count = sum(ind[i] for ind in top_individuals)
        probabilities[i] = ones_count / len(top_individuals)
    return probabilities

# Sample New Individual
def sample_new_individual(probabilities):
    return [1 if random.random() < p else 0 for p in probabilities]

# Main EDA Loop
def eda_knapsack(n, population_size, generations, top_k):
    population = initialize_population(population_size, n)
    best_solution = None
    best_fitness = 0
    generation_count = 0
    optimal_generation = None

    for generation in range(generations):
        generation_count += 1
        top_individuals = select_top_individuals(population, top_k)
        probabilities = learn_distribution(top_individuals, n)
        population = [sample_new_individual(probabilities) for _ in range(population_size)]
        
        current_best = max(population, key=fitness)
        current_fitness = fitness(current_best)
        
        if current_fitness > best_fitness:
            best_solution = current_best
            best_fitness = current_fitness
            optimal_generation = generation_count  # Track the generation when optimal solution is found
        
        # Progress Bar Update
        progress_bar.progress((generation + 1) / generations)

        # Stop early if an optimal solution is found
        if best_fitness == sum(item["Value"] for item in items):
            break

    return best_solution, best_fitness, generation_count, optimal_generation

# Button to Run Optimization
if st.sidebar.button("Find Optimal Solution"):
    progress_bar = st.sidebar.progress(0)
    n = len(items)
    
    # Run EDA Algorithm
    optimal_solution, optimal_fitness, gen_count, optimal_generation = eda_knapsack(n, population_size, generations, top_k)
    
    # Display Results
    st.markdown("### Solution")
    selected_items = [items[i]["Item"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1]
    total_weight = sum(items[i]["Weight"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    total_value = sum(items[i]["Value"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    
    # Display the number of generations it took to find the optimal solution
    if optimal_generation:
        st.markdown(f"**Optimal Solution Found at Generation**: {optimal_generation}")
    else:
        st.markdown(f"**Optimal Solution Not Found in {gen_count} Generations**")

    # Display other results
    st.markdown(f"**Total Weight**: {total_weight} kg")
    st.markdown(f"**Total Value**: {total_value}")
    st.markdown(f"**Selected Items**:")
    st.table(pd.DataFrame([{"Item": item, "Weight": items[df_items[df_items['Item'] == item].index[0]]["Weight"], 
                            "Value": items[df_items[df_items['Item'] == item].index[0]]["Value"]} for item in selected_items]))
