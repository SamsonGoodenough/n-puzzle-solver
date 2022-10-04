import heapq
from lib.graph import Graph
from lib.node import Node

graph = Graph([1,4,2,3,0,5,6,7,8])

graph.discover()

print(graph.goalState)




