import streamlit as st
import random

# Dataset
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

# Problem Parameters
n = len(items)
weights = [item["Weight"] for item in items]
values = [item["Value"] for item in items]

# Fitness Function
def fitness(individual, weight_limit):
    total_weight = sum(individual[i] * weights[i] for i in range(n))
    total_value = sum(individual[i] * values[i] for i in range(n))
    return total_value if total_weight <= weight_limit else 0

# Random Individual
def random_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

# Initialize Population
def initialize_population(pop_size, n):
    return [random_individual(n) for _ in range(pop_size)]

# Select Top k Individuals
def select_top_individuals(population, k, weight_limit):
    return sorted(population, key=lambda ind: fitness(ind, weight_limit), reverse=True)[:k]

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

# EDA Main Loop
def eda_knapsack(n, population_size, generations, top_k, weight_limit):
    population = initialize_population(population_size, n)
    for generation in range(generations):
        top_individuals = select_top_individuals(population, top_k, weight_limit)
        probabilities = learn_distribution(top_individuals, n)
        population = [sample_new_individual(probabilities) for _ in range(population_size)]
        best = max(population, key=lambda ind: fitness(ind, weight_limit))
        best_fitness = fitness(best, weight_limit)
        if best_fitness > 0 and all(p == 1.0 or p == 0.0 for p in probabilities):
            break
    return best

# Streamlit UI
st.title("Knapsack Problem with Estimation of Distribution Algorithm (EDA)")

# Inputs
st.sidebar.header("Knapsack Parameters")
weight_limit = st.sidebar.slider("Weight Limit", min_value=5, max_value=20, value=15)
population_size = st.sidebar.slider("Population Size", min_value=5, max_value=50, value=20)
generations = st.sidebar.slider("Number of Generations", min_value=10, max_value=100, value=50)
top_k = st.sidebar.slider("Top k Individuals", min_value=1, max_value=10, value=5)

# Run EDA
if st.button("Run EDA"):
    best_solution = eda_knapsack(n, population_size, generations, top_k, weight_limit)
    selected_items = [items[i]["Item"] for i in range(n) if best_solution[i] == 1]
    total_value = sum(items[i]["Value"] for i in range(n) if best_solution[i] == 1)
    total_weight = sum(items[i]["Weight"] for i in range(n) if best_solution[i] == 1)

    st.subheader("Results")
    st.write("### Selected Items")
    st.table({"Item": selected_items})
    st.write("### Total Value", total_value)
    st.write("### Total Weight", total_weight)

    st.write("### Full Details")
    for i, item in enumerate(items):
        st.write(f"{item['Item']}: {'Selected' if best_solution[i] else 'Not Selected'}")

# Display Items
st.write("### Items")
st.table(items)
