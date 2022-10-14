from lib.graph import Graph

#TODO: Make sure the path is correct
#TODO: Make work with manhattan distance heuristic and one other heuristic
#TODO: If puzzle given is already solved, print that it is already solved
#TODO: Make work with 15-puzzle
#TODO: Make work with 24-puzzle

#TODO: disorder parameter gives odd number for solvalbe puzzles (e.g. [1,2,3,7,4,5,6,0,8,9,10,11,12,13,14,15])

# graph = Graph([1,2,3,4,
#                0,5,6,7,
#                8,9,10,11,
#                12,13,14,15], "manhattan")
# graph = Graph([1,2,3,7,4,5,6,0,8,9,10,11,12,13,14,15])
graph = Graph([5, 1, 2, 3, 7, 4, 6, 8, 0])
# print(graph.root.state.calculateManhattanDistance())

# graph = Graph([8,6,7,2,5,4,3,0,1])
# graph = Graph([6,4,7,8,5,0,3,2,1])

node = graph.findGoalState()

print("------------------PRINTING PATH TO GOAL STATE------------------")
node.printPath()




