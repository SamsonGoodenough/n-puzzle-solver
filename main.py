from lib.graph import Graph

graph = Graph([1,4,2,3,0,5,6,7,8])
# graph = Graph([7,2,4,5,0,6,8,3,1])

# graph = Graph([8,6,7,2,5,4,3,0,1])
# graph = Graph([6,4,7,8,5,0,3,2,1])

node = graph.discover()

print("------------------PRINTING PATH TO GOAL STATE------------------")
node.printPath()




