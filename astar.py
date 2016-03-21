# Andrew Mayfield
# c542m349
# CS 771 - Artificial Intelligence
# Programming Assignment #1 - n-Puzzle Solver using A* Algorithm

#!usr/bin/env python

from Queue import PriorityQueue
from copy import deepcopy


# This class will hold all the information for each possible state that the puzzle may have.
# value = The current state of the puzzle
# n = The size of the puzzle, e.g. an 8-puzzle would have an n=3
# parent = The parent State that this State was generated from
# start = The start state of the puzzle
# goal = The goal state of the puzzle
# children = List of all children that are possible from the current State
# depth = The depth that this State exists at (g(n))
# cost = The total path cost of this State according to A* algorithm using depth and manhattan distance
# create_children(self): Creates the possible children from current State and adds them to self.children
# manhattan_distance(self): Determines the manhattan distance for the current State when compared to the goal state
class State:
    def __init__(self, value, n, parent=None, start=None, goal=None):
        self.children = []
        self.parent = parent
        self.value = value
        self.n = n
        if parent:
            self.path = deepcopy(parent.path)
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
            self.depth = parent.depth + 1
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
            self.depth = 0
        self.cost = self.depth + self.manhattan_distance()


    def create_children(self):
        if not self.children:
            # Locate the blank tile
            x, y = find_value(0, self.value, self.n)
            # List of possible moves for current value
            possible_moves = ["Up", "Down", "Left", "Right"]
            # Remove impossible moves
            if x == 0:
                # Cannot move Down
                possible_moves.remove("Down")
            elif x == self.n-1:
                #Cannot move Up
                possible_moves.remove("Up")
            if y == 0:
                # Cannot move Left
                possible_moves.remove("Left")
            elif y == self.n-1:
                # Cannot move Right
                possible_moves.remove("Right")

            # Go through all possible moves and create children for each one
            for move in possible_moves:
                if move == "Up":
                    up_value = deepcopy(self.value)
                    swap_places(up_value, x, y, x+1, y)
                    up_child = State(value=up_value, parent=self, n=self.n)
                    self.children.append(up_child)
                if move == "Down":
                    down_value = deepcopy(self.value)
                    swap_places(down_value, x, y, x-1, y)
                    down_child = State(value=down_value, parent=self, n=self.n)
                    self.children.append(down_child)
                if move == "Left":
                    left_value = deepcopy(self.value)
                    swap_places(left_value, x, y, x, y-1)
                    left_child = State(value=left_value, parent=self, n=self.n)
                    self.children.append(left_child)
                if move == "Right":
                    right_value = deepcopy(self.value)
                    swap_places(right_value, x, y, x, y+1)
                    right_child = State(value=right_value, parent=self, n=self.n)
                    self.children.append(right_child)


    def manhattan_distance(self):
        if self.value == self.goal:
            return 0
        total = 0
        for x1 in range(self.n):
            for y1 in range(self.n):
                value = self.value[x1][y1]
                if value == 0:
                    continue
                x2, y2 = find_value(value, self.goal, self.n)
                total += (abs(x1-x2) + abs(y1-y2))
        return total

# Finds the location of a value in a state
def find_value(value, state, n):
    for x in range(n):
        for y in range(n):
            if state[x][y] == value:
                return x, y


# Swaps two different values in a state when given their locations
def swap_places(state, x1, y1, x2, y2):
    val1 = state[x1][y1]
    val2 = state[x2][y2]
    state[x1][y1] = val2
    state[x2][y2] = val1
    return state


# The A* Algorithm class
class Astar:
    def __init__(self, start, goal, n):
        self.path = []
        self. visited = []
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal
        self.n = n

    def solve(self):
        start_state = State(value=self.start, start=self.start, goal=self.goal, n=self.n)

        self.priority_queue.put((0, start_state))
        while(not self.path and self.priority_queue.qsize()):
            closest_child = self.priority_queue.get()[1]
            closest_child.create_children()
            self.visited.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visited:
                    # If child's value is equal to goal, solution is found
                    if child.value == self.goal:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.cost, child))
        if not self.path:
            print "Goal is unreachable. Terminating program."
        return self.path


# Main function that runs the (n^2-1)-Puzzle Solver
def main(example=False):
    print "Welcome to the n-puzzle solver."
    print "This program will solve an n-puzzle after it is given an initial state and a goal state."

    # If the program is run with example set to True, then it will use this example.
    if example:
        n = 3
        start = [[7, 0, 5], [1, 6, 4], [2, 8, 3]]
        goal =  [[7, 6, 5], [8, 0, 4], [1, 2, 3]]

        # start = [[6, 7, 8], [3, 4, 5], [1, 0, 2]]
        # goal =  [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
    else:
        # Puzzle Size
        n = int(input("What size is your puzzle in terms of n (ex: 8, 15, 24, etc.): "))

        start = [[0]*n for i in range(n)]
        goal = [[0]*n for i in range(n)]

        print "When entering the start and goal states, use 0 as the value for the blank tile."

        # Ask user for goal state
        print "First, enter your puzzle's goal state."
        for x in range(n):
            for y in range(n):
                value = input("Enter value for the tile located at ({0}, {1}) coordinate position for goal configuration: ".format(x, y))
                goal[x][y] = value

        # Ask user for initial state
        print "Next, enter your puzzle's initial state."
        for x in range(n):
            for y in range(n):
                value = input("Enter value for the tile located at ({0}, {1}) coordinate position for start configuration: ".format(x, y))
                start[x][y] = value

    print "The program will now solve your {0}-puzzle.\n".format(n**2 - 1)

    print "Start State:"
    for x in range(n-1, -1, -1):
        print start[x]
    print "Goal State:"
    for x in range(n-1, -1, -1):
        print goal[x]

    if start == goal:
        print "Problem is already solved. Exiting program."
        return

    a = Astar(start, goal, n)
    a.solve()

    print "\n\nThe full solution path is shown below:"
    for i in range(len(a.path)):
        print "Step {0})".format(i)
        for x in range(n-1, -1, -1):
            print a.path[i][x]
        print ""


# Run the program
main(example=True)
