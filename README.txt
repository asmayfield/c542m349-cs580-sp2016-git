#New Comment
Andrew Mayfield
c542m349
CS 771 - Artificial Intelligence
Programming Assignment #1 - n-Puzzle Solver using A* Algorithm

#######################
# PROGRAM DESCRIPTION #
#######################
This program will solve an (n^2-1)-puzzle with a user entered start and goal state.
The program will first ask the user for the size of the puzzle in terms of n:
  For example: For an 8-Puzzle, the user would enter 3 when prompted.
The user is then prompted to enter a goal state.
The user is lastly prompted to enter the start state.

The States are designed so that the bottom left corner is location (0,0) and the top right corner is location (n-1, n-1).

The program will use the A* Algorithm using the node's depth as it's path cost [g(n)] and it's Manhattan Distance as it's heuristic [h(n)].
  PATH-COST = f(n) + g(n)
  f(n) = depth
  g(n) = Manhattan Distance

If the problem is solvable, the program will output the full path it took to reach the goal state beginning with the start state.
If the problem is not solvable, then the program will run until it exhausts every possible State and then it will output that the problem is not solvable with the given start and goal states.


#######################
# RUNNING THE PROGRAM #
#######################
This program is written in Python 2.7.
It can be run using the following command on the Linux Labs at WSU:
  python astar.py

The program will come with an example problem (n, start, and goal state), and this can be run by changing the argument "example" in the main method to True.
  main(example=True)
To disable the example and enter a user defined n, start, and goal state, set the "example" argument to False:
  main(example=False)

When the example is disabled, the program will ask for user input for 3 variables:
  n: This is the size of the puzzle (nxn grid)
  start: This is the start state of the puzzle, entered one value at a time
  goal: This is the goal state of the puzzle, entered one value at a time


###################
# EXAMPLE PROBLEM #
###################
For the example problem in the code, the output will look like:
  Welcome to the n-puzzle solver.
  This program will solve an n-puzzle after it is given an initial state and a goal state.
  The program will now solve your 8-puzzle.

  Start State:
  [2, 8, 3]
  [1, 6, 4]
  [7, 0, 5]
  Goal State:
  [1, 2, 3]
  [8, 0, 4]
  [7, 6, 5]


  The full solution path is shown below:
  Step 0)
  [2, 8, 3]
  [1, 6, 4]
  [7, 0, 5]

  Step 1)
  [2, 8, 3]
  [1, 0, 4]
  [7, 6, 5]

  Step 2)
  [2, 0, 3]
  [1, 8, 4]
  [7, 6, 5]

  Step 3)
  [0, 2, 3]
  [1, 8, 4]
  [7, 6, 5]

  Step 4)
  [1, 2, 3]
  [0, 8, 4]
  [7, 6, 5]

  Step 5)
  [1, 2, 3]
  [8, 0, 4]
  [7, 6, 5]
