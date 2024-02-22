import math

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate(), None
    
    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            if max_eval > alpha:
                alpha = max_eval
                best_move = child.move
            if alpha >= beta:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            if min_eval < beta:
                beta = min_eval
                best_move = child.move
            if alpha >= beta:
                break
        return min_eval, best_move

# Example of usage:
class Node:
    def __init__(self, move):
        self.move = move
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_terminal(self):
        return len(self.children) == 0

    def generate_children(self):
        return self.children

    def evaluate(self):
        # Your evaluation function here
        return 0

# Example of usage
root = Node(None)
child1 = Node('A')
child2 = Node('B')
child3 = Node('C')

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(Node('D'))
child1.add_child(Node('E'))
child2.add_child(Node('F'))
child2.add_child(Node('G'))
child3.add_child(Node('H'))
child3.add_child(Node('I'))

score, best_move = alpha_beta_pruning(root, 3, -math.inf, math.inf, True)
print("Best move:", best_move)
print("Score:", score)
