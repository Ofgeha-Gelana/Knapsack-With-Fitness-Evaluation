import streamlit as st
import pandas as pd
from optimization import eda_knapsack
from data import items
from utils import initialize_population, fitness, select_top_individuals

# Problem Statement
st.title("🧳 Knapsack Problem - Trip Packing Optimization")
st.markdown("""
### Problem Statement:
You are preparing for a trip and have a set of items, each with a weight and a value. The goal is to select the most valuable combination of items that fit into your bag without exceeding its weight capacity.

Use the parameters in the sidebar to adjust the weight limit and population size, and click the button to find the optimal solution.
""")

df_items = pd.DataFrame(items)
st.markdown("### Available Items")
st.table(df_items)

# Sidebar for Parameters
st.sidebar.header("Parameters")
weight_limit = st.sidebar.slider("Weight Limit (kg)", 5.0, 20.0, 15.0, 0.5)
population_size = st.sidebar.slider("Population Size", 5, 50, 20, 1)
generations = st.sidebar.slider("Generations", 10, 100, 30, 5)
top_k = st.sidebar.slider("Top K (Selection Pool)", 1, population_size, 5, 1)

# Button to Run Optimization
if st.sidebar.button("Find Optimal Solution"):
    progress_bar = st.sidebar.progress(0)
    n = len(items)
    
    # Run EDA Algorithm
    optimal_solution, optimal_fitness, gen_count, optimal_generation = eda_knapsack(
        n, population_size, generations, top_k, weight_limit, items, progress_bar
    )
    
    # Display Results
    st.markdown("### Solution")
    selected_items = [items[i]["Item"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1]
    total_weight = sum(items[i]["Weight"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    total_value = sum(items[i]["Value"] for i in range(len(optimal_solution)) if optimal_solution[i] == 1)
    
    if optimal_generation:
        st.markdown(f"**Optimal Solution Found at Generation**: {optimal_generation}")
    else:
        st.markdown(f"**Optimal Solution Not Found in {gen_count} Generations**")

    st.markdown(f"**Total Weight**: {total_weight} kg")
    st.markdown(f"**Total Value**: {total_value}")
    st.markdown(f"**Selected Items**:")
    st.table(pd.DataFrame([
        {"Item": item, "Weight": items[df_items[df_items['Item'] == item].index[0]]["Weight"], 
         "Value": items[df_items[df_items['Item'] == item].index[0]]["Value"]} 
        for item in selected_items
    ]))
