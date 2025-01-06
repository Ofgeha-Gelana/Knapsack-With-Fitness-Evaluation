# Knapsack Problem Using Estimation of Distribution Algorithm (EDA)

This project solves the classic **Knapsack Problem** using an **Estimation of Distribution Algorithm (EDA)**. It demonstrates how to maximize the total value of items that can fit into a knapsack with a given weight capacity while maintaining interactivity through a Streamlit dashboard.

---

## Problem Statement

Imagine you're planning a trip and need to pack items into a bag with limited capacity. Each item has a specific weight and value. Your goal is to select items that maximize the value of your packed bag without exceeding its weight limit.

---

## Features

### 🛠 Functionalities
- **Interactive Dashboard:** Adjust parameters like weight capacity and population size from the sidebar.
- **Dynamic Visualization:** Observe the algorithm evolve over generations to find the optimal solution.
- **Results Table:** Displays the selected items with their weight, value, and total metrics.
- **Data Insights:** View the dataset of available items and experiment with different configurations.

### ⚙️ Parameters (Set in Sidebar)
1. **Knapsack Capacity:** The maximum weight the bag can carry.
2. **Population Size:** Number of solutions in each generation.
3. **Top Individuals:** Number of top-performing solutions used to learn the probability distribution.
4. **Generations:** Number of iterations for the algorithm to evolve.
5. **Toggle Early Termination:** disable stopping early when the best solution is found.

---

## How It Works

The **Estimation of Distribution Algorithm (EDA)** works as follows:
1. **Initialization:** Randomly generate solutions (populations of items) within the weight limit.
2. **Fitness Evaluation:** Calculate the total value of items in each solution.
3. **Selection:** Choose the top-performing solutions to learn a probability distribution.
4. **Sampling:** Generate new solutions based on the learned distribution.
5. **Evolution:** Repeat the process for the specified number of generations or until the optimal solution is found.

---

## Interactive Demo

You can interact with the live demo of the Knapsack problem using the Estimation of Distribution Algorithm here:

[**Interactive Demo - Knapsack EDA**](https://knapsack-with-fitness-evaluation.streamlit.app/)

---
[Screenshot of Demo - Knapsack EDA](https://raw.githubusercontent.com/Ofgeha-Gelana/Knapsack-With-Fitness-Evaluation/refs/heads/main/app/Screenshot%202025-01-06%20045001.png)

---
## How to Run the Project

### 📦 Prerequisites
- Python 3.8 or later
- Streamlit library
- Install other dependencies listed in `requirements.txt` (if available)

### 🚀 Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/knapsack-eda.git
   cd knapsack-eda
