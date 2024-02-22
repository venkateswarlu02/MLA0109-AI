import random
import math

def simulated_annealing(cost_function, initial_solution, temperature, cooling_rate, stopping_temperature):
    current_solution = initial_solution
    current_cost = cost_function(current_solution)
    
    while temperature > stopping_temperature:
        new_solution = neighbor(current_solution)
        new_cost = cost_function(new_solution)
        
        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost
        else:
            probability = acceptance_probability(current_cost, new_cost, temperature)
            if random.random() < probability:
                current_solution = new_solution
                current_cost = new_cost
                
        temperature *= cooling_rate
    
    return current_solution, current_cost

def neighbor(solution):
    # This function generates a neighboring solution
    # For demonstration purposes, it just swaps two random elements
    new_solution = solution[:]
    idx1 = random.randint(0, len(solution) - 1)
    idx2 = random.randint(0, len(solution) - 1)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0
    else:
        return math.exp((current_cost - new_cost) / temperature)

def cost_function(solution):
    # This is the objective function to be minimized
    # For demonstration purposes, it just returns the sum of the solution
    return sum(solution)

# Example usage
if __name__ == "__main__":
    initial_solution = [1, 2, 3, 4, 5]  # Initial solution
    initial_temperature = 1000  # Initial temperature
    cooling_rate = 0.95  # Cooling rate
    stopping_temperature = 0.001  # Stopping temperature

    final_solution, final_cost = simulated_annealing(cost_function, initial_solution, initial_temperature, cooling_rate, stopping_temperature)

    print("Final solution:", final_solution)
    print("Final cost:", final_cost)
