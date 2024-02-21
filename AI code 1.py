import itertools

class SlidingPuzzle:
    def __init__(self, initial_state):
        self.size = int(len(initial_state) ** 0.5)
        self.goal_state = tuple(range(1, self.size**2)) + (0,)
        self.initial_state = initial_state

    def get_neighbors(self, state):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        zero_index = state.index(0)
        zero_row, zero_col = zero_index // self.size, zero_index % self.size
        neighbors = []
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                new_index = new_row * self.size + new_col
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))
        return neighbors

    def solve(self):
        queue = [(self.initial_state, 0)]
        visited = set()
        while queue:
            state, steps = queue.pop(0)
            if state == self.goal_state:
                return steps
            if state not in visited:
                visited.add(state)
                queue.extend((neighbor, steps + 1) for neighbor in self.get_neighbors(state))
        return -1  # No solution

# Example usage:
initial_state = (1, 2, 3, 0, 4, 5, 6, 7, 8)
puzzle = SlidingPuzzle(initial_state)
steps_to_solve = puzzle.solve()
print("Steps to solve:", steps_to_solve)
