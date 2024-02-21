class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return f"Node: {self.state}"

def best_first_search(initial_state, goal_test, successors, heuristic):
    frontier = []
    explored = set()

    frontier.append(Node(initial_state, None, None, 0))

    while frontier:
        frontier.sort(key=lambda x: heuristic(x.state))
        node = frontier.pop(0)

        if goal_test(node.state):
            return node

        explored.add(node.state)

        for successor, action, cost in successors(node.state):
            if successor not in explored:
                frontier.append(Node(successor, node, action, cost))

    return None

# Example usage:
# Define the heuristic function
def heuristic(state):
    # Here you can define your own heuristic for the specific problem
    # This heuristic should estimate the cost to reach the goal from the given state
    # For example, for a grid-based problem, it could be the Manhattan distance to the goal
    return 0

# Define the goal test function
def goal_test(state):
    # Here you define the condition to check if the given state is a goal state
    # For example, if the state matches the desired configuration of the puzzle/grid
    return False

# Define the successors function
def successors(state):
    # Here you define how to generate successor states from the given state
    # This function should return a list of tuples (successor_state, action, cost)
    # For example, for a grid-based problem, it could return all possible moves
    return []

# Example usage:
initial_state = None  # Define your initial state here
goal_node = best_first_search(initial_state, goal_test, successors, heuristic)

# Once you have the goal node, you can retrieve the path from the initial state to the goal state
if goal_node:
    path = []
    while goal_node:
        path.append(goal_node)
        goal_node = goal_node.parent
    path.reverse()
    for node in path:
        print(node)
else:
    print("Goal not found")
