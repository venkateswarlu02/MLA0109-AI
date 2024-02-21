class RiverCrossingPuzzle:
    def __init__(self):
        self.state = (3, 3, 1)  # (missionaries on the initial side, cannibals on the initial side, boat position)
        self.moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]  # possible moves of the boat

    def is_valid_state(self, state):
        m, c, b = state
        if m < 0 or c < 0 or m > 3 or c > 3 or (m != 0 and m < c) or (m != 3 and m > c):
            return False
        return True

    def get_next_states(self, state):
        next_states = []
        m, c, b = state
        for move in self.moves:
            if b == 1:
                new_state = (m - move[0], c - move[1], 0)
            else:
                new_state = (m + move[0], c + move[1], 1)
            if self.is_valid_state(new_state):
                next_states.append(new_state)
        return next_states

    def solve(self):
        visited = set()
        queue = [[self.state]]
        while queue:
            path = queue.pop(0)
            current_state = path[-1]
            if current_state[0] == 0 and current_state[1] == 0 and current_state[2] == 0:
                return path
            for next_state in self.get_next_states(current_state):
                if next_state not in visited:
                    visited.add(next_state)
                    new_path = list(path)
                    new_path.append(next_state)
                    queue.append(new_path)
        return None

    def print_solution(self, solution):
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: Missionaries: {state[0]}, Cannibals: {state[1]}, Boat: {'Right' if state[2] == 1 else 'Left'}")

if __name__ == "__main__":
    puzzle = RiverCrossingPuzzle()
    solution = puzzle.solve()
    if solution:
        print("Solution found:")
        puzzle.print_solution(solution)
    else:
        print("No solution found.")
