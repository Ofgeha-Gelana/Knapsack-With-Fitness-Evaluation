# import streamlit as st
# import random

# # Dataset
# items = [
#     {"Item": "Tent", "Weight": 5.0, "Value": 10},
#     {"Item": "Sleeping Bag", "Weight": 3.5, "Value": 7},
#     {"Item": "Cooking Kit", "Weight": 4.0, "Value": 8},
#     {"Item": "First Aid Kit", "Weight": 1.0, "Value": 6},
#     {"Item": "Water Bottle", "Weight": 2.0, "Value": 9},
#     {"Item": "Clothes", "Weight": 3.0, "Value": 5},
#     {"Item": "Flashlight", "Weight": 1.5, "Value": 3},
#     {"Item": "Power Bank", "Weight": 1.0, "Value": 4},
#     {"Item": "Snacks", "Weight": 2.5, "Value": 6},
#     {"Item": "Notebook & Pen", "Weight": 0.5, "Value": 2},
# ]

# # Problem Parameters
# n = len(items)
# weights = [item["Weight"] for item in items]
# values = [item["Value"] for item in items]

# # Fitness Function
# def fitness(individual, weight_limit):
#     total_weight = sum(individual[i] * weights[i] for i in range(n))
#     total_value = sum(individual[i] * values[i] for i in range(n))
#     return total_value if total_weight <= weight_limit else 0

# # Random Individual
# def random_individual(n):
#     return [random.randint(0, 1) for _ in range(n)]

# # Initialize Population
# def initialize_population(pop_size, n):
#     return [random_individual(n) for _ in range(pop_size)]

# # Select Top k Individuals
# def select_top_individuals(population, k, weight_limit):
#     return sorted(population, key=lambda ind: fitness(ind, weight_limit), reverse=True)[:k]

# # Learn Distribution
# def learn_distribution(top_individuals, n):
#     probabilities = [0.0] * n
#     for i in range(n):
#         ones_count = sum(ind[i] for ind in top_individuals)
#         probabilities[i] = ones_count / len(top_individuals)
#     return probabilities

# # Sample New Individual
# def sample_new_individual(probabilities):
#     return [1 if random.random() < p else 0 for p in probabilities]

# # EDA Main Loop
# def eda_knapsack(n, population_size, generations, top_k, weight_limit):
#     population = initialize_population(population_size, n)
#     for generation in range(generations):
#         top_individuals = select_top_individuals(population, top_k, weight_limit)
#         probabilities = learn_distribution(top_individuals, n)
#         population = [sample_new_individual(probabilities) for _ in range(population_size)]
#         best = max(population, key=lambda ind: fitness(ind, weight_limit))
#         best_fitness = fitness(best, weight_limit)
#         if best_fitness > 0 and all(p == 1.0 or p == 0.0 for p in probabilities):
#             break
#     return best

# # Streamlit UI
# st.title("Knapsack Problem with Estimation of Distribution Algorithm (EDA)")

# # Inputs
# st.sidebar.header("Knapsack Parameters")
# weight_limit = st.sidebar.slider("Weight Limit", min_value=5, max_value=20, value=15)
# population_size = st.sidebar.slider("Population Size", min_value=5, max_value=50, value=20)
# generations = st.sidebar.slider("Number of Generations", min_value=10, max_value=100, value=50)
# top_k = st.sidebar.slider("Top k Individuals", min_value=1, max_value=10, value=5)

# # Run EDA
# if st.button("Run EDA"):
#     best_solution = eda_knapsack(n, population_size, generations, top_k, weight_limit)
#     selected_items = [items[i]["Item"] for i in range(n) if best_solution[i] == 1]
#     total_value = sum(items[i]["Value"] for i in range(n) if best_solution[i] == 1)
#     total_weight = sum(items[i]["Weight"] for i in range(n) if best_solution[i] == 1)

#     st.subheader("Results")
#     st.write("### Selected Items")
#     st.table({"Item": selected_items})
#     st.write("### Total Value", total_value)
#     st.write("### Total Weight", total_weight)

#     st.write("### Full Details")
#     for i, item in enumerate(items):
#         st.write(f"{item['Item']}: {'Selected' if best_solution[i] else 'Not Selected'}")

# # Display Items
# st.write("### Items")
# st.table(items)







# import streamlit as st
# import random

# # Problem Statement
# st.title("🧳 Knapsack Problem - Trip Packing Optimization")
# st.markdown("""
# ### Problem Statement:
# Imagine you're going on a trip, and you need to pack a bag. Your goal is to pack as many valuable items as possible, but your bag has a weight limit. 
# Given a set of items, each with a weight and a value, the task is to determine the combination of items that fits into the bag without exceeding the weight limit, 
# while maximizing the total value of the selected items.

# #### Input:
# - A list of items with their weight and value.
# - A weight limit for the bag (capacity).

# The goal is to find the best subset of items that maximizes the value without exceeding the capacity of your bag.
# """)

# # Data: Items with their weight and value
# items = [
#     {"Item": "Tent", "Weight": 5.0, "Value": 10},
#     {"Item": "Sleeping Bag", "Weight": 3.5, "Value": 7},
#     {"Item": "Cooking Kit", "Weight": 4.0, "Value": 8},
#     {"Item": "First Aid Kit", "Weight": 1.0, "Value": 6},
#     {"Item": "Water Bottle", "Weight": 2.0, "Value": 9},
#     {"Item": "Clothes", "Weight": 3.0, "Value": 5},
#     {"Item": "Flashlight", "Weight": 1.5, "Value": 3},
#     {"Item": "Power Bank", "Weight": 1.0, "Value": 4},
#     {"Item": "Snacks", "Weight": 2.5, "Value": 6},
#     {"Item": "Notebook & Pen", "Weight": 0.5, "Value": 2},
# ]

# # Display available items in the sidebar
# st.sidebar.header("Available Items")
# item_names = [item["Item"] for item in items]
# for item in items:
#     st.sidebar.write(f"**{item['Item']}** - Weight: {item['Weight']} | Value: {item['Value']}")

# # User input: Knapsack capacity (weight limit)
# weight_limit = st.sidebar.number_input("Enter your bag's weight limit (capacity):", min_value=1.0, value=10.0, step=0.5)

# # Fitness Function: Calculate total value for selected items
# def fitness(selected_items):
#     total_weight = sum(item["Weight"] for item in selected_items)
#     total_value = sum(item["Value"] for item in selected_items)
#     return total_weight, total_value

# # Solution Function: Greedy Knapsack Solver
# def greedy_knapsack(items, weight_limit):
#     # Sort items by value-to-weight ratio
#     items_sorted = sorted(items, key=lambda x: x["Value"] / x["Weight"], reverse=True)
#     selected_items = []
#     total_weight = 0

#     for item in items_sorted:
#         if total_weight + item["Weight"] <= weight_limit:
#             selected_items.append(item)
#             total_weight += item["Weight"]

#     total_value = sum(item["Value"] for item in selected_items)
#     return selected_items, total_weight, total_value

# # Solve the Knapsack problem
# selected_items, total_weight, total_value = greedy_knapsack(items, weight_limit)

# # Display the result
# st.markdown("### Solution: Best Combination of Items")
# st.write(f"#### Total Value: **{total_value}**")
# st.write(f"#### Total Weight: **{total_weight}** (Weight Limit: {weight_limit})")

# # Display the selected items
# st.write("#### Selected Items:")
# selected_items_data = [{"Item": item["Item"], "Weight": item["Weight"], "Value": item["Value"]} for item in selected_items]
# st.dataframe(selected_items_data, use_container_width=True)

# # Display the full list of items with their weight and value
# st.write("#### Full List of Items with Selection Status:")
# for item in items:
#     selection_status = "Selected" if item in selected_items else "Not Selected"
#     st.write(f"**{item['Item']}** - {selection_status} | Weight: {item['Weight']} | Value: {item['Value']}")

# # Display the problem and solution in a professional format
# st.markdown("""
# ### Problem Recap:
# Given a set of items, each with a weight and value, the task is to determine the combination of items that maximizes the value without exceeding the weight limit. 
# The solution was found using a **Greedy Algorithm**, which selects items based on the highest value-to-weight ratio until the weight limit is reached.

# #### Your Optimal Trip Packing:
# - You've packed the items with the best value-to-weight ratio that fit within your bag's capacity.
# - Total weight and total value are shown above.
# """)

# # Display interactive widgets to modify the problem
# st.sidebar.markdown("### Modify the Problem")
# st.sidebar.write("Change the weight limit to see how the solution changes.")




# import streamlit as st

# # Problem Statement
# st.title("🧳 Knapsack Problem - Trip Packing Optimization")
# st.markdown("""
# ### Problem Statement:
# Imagine you're going on a trip, and you need to pack a bag. Your goal is to pack as many valuable items as possible, but your bag has a weight limit. 
# Given a set of items, each with a weight and a value, the task is to determine the combination of items that fits into the bag without exceeding the weight limit, 
# while maximizing the total value of the selected items.

# #### Input:
# - A list of items with their weight and value.
# - A weight limit for the bag (capacity).

# The goal is to find the best subset of items that maximizes the value without exceeding the capacity of your bag.
# """)

# # Data: Items with their weight and value
# items = [
#     {"Item": "Tent", "Weight": 5.0, "Value": 10},
#     {"Item": "Sleeping Bag", "Weight": 3.5, "Value": 7},
#     {"Item": "Cooking Kit", "Weight": 4.0, "Value": 8},
#     {"Item": "First Aid Kit", "Weight": 1.0, "Value": 6},
#     {"Item": "Water Bottle", "Weight": 2.0, "Value": 9},
#     {"Item": "Clothes", "Weight": 3.0, "Value": 5},
#     {"Item": "Flashlight", "Weight": 1.5, "Value": 3},
#     {"Item": "Power Bank", "Weight": 1.0, "Value": 4},
#     {"Item": "Snacks", "Weight": 2.5, "Value": 6},
#     {"Item": "Notebook & Pen", "Weight": 0.5, "Value": 2},
# ]

# # Display available items as a table in the main dashboard
# st.markdown("### Available Items")
# st.table(items)

# # Sidebar for user input
# st.sidebar.header("Parameters")
# weight_limit = st.sidebar.number_input(
#     "Enter your bag's weight limit (capacity):", min_value=1.0, value=10.0, step=0.5
# )
# solve_button = st.sidebar.button("Get Solution")

# # Fitness Function: Calculate total value for selected items
# def fitness(selected_items):
#     total_weight = sum(item["Weight"] for item in selected_items)
#     total_value = sum(item["Value"] for item in selected_items)
#     return total_weight, total_value

# # Solution Function: Greedy Knapsack Solver
# def greedy_knapsack(items, weight_limit):
#     # Sort items by value-to-weight ratio
#     items_sorted = sorted(items, key=lambda x: x["Value"] / x["Weight"], reverse=True)
#     selected_items = []
#     total_weight = 0

#     for item in items_sorted:
#         if total_weight + item["Weight"] <= weight_limit:
#             selected_items.append(item)
#             total_weight += item["Weight"]

#     total_value = sum(item["Value"] for item in selected_items)
#     return selected_items, total_weight, total_value

# # Solve the Knapsack problem when button is clicked
# if solve_button:
#     selected_items, total_weight, total_value = greedy_knapsack(items, weight_limit)

#     # Display the result
#     st.markdown("### Solution: Best Combination of Items")
#     st.write(f"#### Total Value: **{total_value}**")
#     st.write(f"#### Total Weight: **{total_weight}** (Weight Limit: {weight_limit})")

#     # Display the selected items
#     st.markdown("#### Selected Items:")
#     selected_items_data = [
#         {"Item": item["Item"], "Weight": item["Weight"], "Value": item["Value"]}
#         for item in selected_items
#     ]
#     st.table(selected_items_data)

#     # Display the full list of items with selection status
#     st.markdown("#### Full List of Items with Selection Status:")
#     all_items_data = [
#         {
#             "Item": item["Item"],
#             "Weight": item["Weight"],
#             "Value": item["Value"],
#             "Status": "Selected" if item in selected_items else "Not Selected",
#         }
#         for item in items
#     ]
#     st.table(all_items_data)








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
        
        # Progress Bar Update
        progress_bar.progress((generation + 1) / generations)

        # Stop early if an optimal solution is found
        if best_fitness == sum(item["Value"] for item in items):
            break

    return best_solution, best_fitness, generation_count

# Button to Run Optimization
if st.sidebar.button("Find Optimal Solution"):
    progress_bar = st.sidebar.progress(0)
    n = len(items)
    
    # Run EDA Algorithm
    optimal_solution, optimal_fitness, gen_count = eda_knapsack(n, population_size, generations, top_k)
    
    # Display Results
    st.markdown("### Solution")
    selected_items = [items[i]["Item"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1]
    total_weight = sum(items[i]["Weight"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    total_value = sum(items[i]["Value"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    
    st.markdown(f"**Generations Taken**: {gen_count}")
    st.markdown(f"**Total Weight**: {total_weight} kg")
    st.markdown(f"**Total Value**: {total_value}")
    st.markdown(f"**Selected Items**:")
    st.table(pd.DataFrame([{"Item": item, "Weight": items[df_items[df_items['Item'] == item].index[0]]["Weight"], 
                            "Value": items[df_items[df_items['Item'] == item].index[0]]["Value"]} for item in selected_items]))
