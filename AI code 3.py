class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()

    def pour_water(self, jug1, jug2):
        if (jug1, jug2) in self.visited:
            return False
        self.visited.add((jug1, jug2))
        
        if jug1 == self.target or jug2 == self.target:
            return True

        # Fill jug1
        if jug1 < self.jug1_capacity:
            if self.pour_water(self.jug1_capacity, jug2):
                print(f"Fill {self.jug1_capacity}-gallon jug")
                return True

        # Fill jug2
        if jug2 < self.jug2_capacity:
            if self.pour_water(jug1, self.jug2_capacity):
                print(f"Fill {self.jug2_capacity}-gallon jug")
                return True

        # Empty jug1
        if jug1 > 0:
            if self.pour_water(0, jug2):
                print("Empty jug1")
                return True

        # Empty jug2
        if jug2 > 0:
            if self.pour_water(jug1, 0):
                print("Empty jug2")
                return True

        # Pour from jug1 to jug2
        if jug1 > 0 and jug2 < self.jug2_capacity:
            amount = min(jug1, self.jug2_capacity - jug2)
            if self.pour_water(jug1 - amount, jug2 + amount):
                print(f"Pour {amount}-gallon from jug1 to jug2")
                return True

        # Pour from jug2 to jug1
        if jug2 > 0 and jug1 < self.jug1_capacity:
            amount = min(jug2, self.jug1_capacity - jug1)
            if self.pour_water(jug1 + amount, jug2 - amount):
                print(f"Pour {amount}-gallon from jug2 to jug1")
                return True

        return False

    def solve(self):
        if self.pour_water(0, 0):
            print("Solution found.")
        else:
            print("No solution found.")


if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    water_jug = WaterJug(jug1_capacity, jug2_capacity, target)
    water_jug.solve()
