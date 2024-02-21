class EightQueens:
    def __init__(self, n=8):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def solve_queens(self, col):
        if col >= self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.solve_queens(col + 1)
                self.board[i][col] = 0
        return False

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()


if __name__ == "__main__":
    n = 8
    queens = EightQueens(n)
    queens.solve_queens(0)
    print("Number of solutions:", len(queens.solutions))
    queens.print_solutions()
