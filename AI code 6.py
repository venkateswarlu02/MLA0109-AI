class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()

    def is_valid_cell(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def clean(self, row, col):
        if not self.is_valid_cell(row, col) or (row, col) in self.visited:
            return
        self.visited.add((row, col))
        if self.grid[row][col] == 'dirty':
            print(f"Cleaning cell ({row}, {col})")
            self.grid[row][col] = 'clean'
        self.clean(row + 1, col)
        self.clean(row - 1, col)
        self.clean(row, col + 1)
        self.clean(row, col - 1)

    def clean_all(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.clean(i, j)

# Example usage:
grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'dirty', 'clean'],
    ['dirty', 'clean', 'clean', 'dirty']
]

vacuum = VacuumCleaner(grid)
vacuum.clean_all()
