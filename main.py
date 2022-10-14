from lib.graph import Graph
import random

#TODO: Make sure the path is correct
#TODO: Make work with manhattan distance heuristic and one other heuristic
#TODO: If puzzle given is already solved, print that it is already solved
#TODO: Make work with 15-puzzle
#TODO: Make work with 24-puzzle

#TODO: disorder parameter gives odd number for solvalbe puzzles (e.g. [1,2,3,7,4,5,6,0,8,9,10,11,12,13,14,15])

def randomize8Puzzle(heuristic):
    graphs = []
    for i in range(100):
        puzzle = [1,2,3,4,5,6,7,8,0]
        random.shuffle(puzzle)
        graph = Graph(puzzle, heuristic)
        while(not graph.solvable and graph not in graphs):
            random.shuffle(puzzle)
            graph = Graph(puzzle)
        graphs.append(graph)
    return graphs

def randomize15Puzzle(heuristic):
    graphs = []
    for i in range(100):
        puzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        random.shuffle(puzzle)
        graph = Graph(puzzle, heuristic)
        while(not graph.solvable and graph not in graphs):
            random.shuffle(puzzle)
            graph = Graph(puzzle)
        graphs.append(graph)
    return graphs
    

def randomize24Puzzle(heuristic):
    graphs = []
    for i in range(100):
        puzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
        random.shuffle(puzzle)
        graph = Graph(puzzle, heuristic)
        while(not graph.solvable and graph not in graphs):
            random.shuffle(puzzle)
            graph = Graph(puzzle)
        graphs.append(graph)
    return graphs


graph = Graph([1,2,3,7,
               0,5,6,4,
               8,9,10,11,
               12,13,14,15], "manhattan") # this one actually works!! wow!!
# graph = Graph([1,2,3,4,
#                5,6,7,8,
#                0,9,10,11,
#                12,13,14,15], "manhattan")
# print(graph.root.state.calculateDisorder())
# graph = Graph([10,3,8,7,2,6,4,12,5,13,9,0,1,14,11,15], "manhattan")
# graph = Graph([4, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "manhattan")
# node = graph.findGoalState()
# node.printPath()
# graph = Graph([4, 1, 2, 3, 8, 5, 6, 7, 0, 9, 10, 11, 12, 13, 14, 15], "manhattan")
# node = graph.findGoalState()
# node.printPath()
# graph = Graph([4, 1, 2, 3, 8, 5, 6, 7, 12, 9, 10, 11, 0, 13, 14, 15], "manhattan")
# node = graph.findGoalState()
# node.printPath()

# graph = Graph([1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,0], "manhattan") # the configuration of the devil
# graph = Graph([1,7,3,4,6,2,15,14,5,11,0,12,10,9,8,13], "manhattan")
# print(graph.root.state.calculateDisorder())
# graph = Graph([5, 1, 2, 3, 7, 4, 6, 8, 0])

# graph = Graph([8,6,7,2,5,4,3,0,1], "manhattan")
# graph = Graph([6,4,7,8,5,0,3,2,1])
# puzzles = randomize8Puzzle()

# i = 0
# totalExpands = 0
# totalExplored = 0
# for graph in randomize15Puzzle("manhattan"):
#     print("Puzzle " + str(i))
#     i += 1
#     graph.findGoalState()
#     totalExpands += graph.expanded
#     totalExplored += len(graph.explored)
# print("EXPAND AVG: ", totalExpands/100.0)
# print("EXPLORED AVG: ", totalExplored/100.0)

node = graph.findGoalState()
print(node)
print("------------------PRINTING PATH TO GOAL STATE------------------")
node.printPath()




