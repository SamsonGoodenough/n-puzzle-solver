import heapq
import math
from .state import State
from .node import Node
import time

class Graph:
  """
  ----------------------------------------------------------
  Graph class
  Use: Holds the root state and goal state of the graph.
  ----------------------------------------------------------
  Parameters:
    id                  : ID of the root state. (Array)
    heuristic           : Heuristic to use when calculating the cost of a node. Default is misplaced tiles (String)
  Variables:
    goalState           : Goal state of the graph. (State)
    heuristic           : Heuristic to use when calculating the cost of a node. Default is misplaced tiles (String)
    explored            : Dictionary of explored states. (Dictionary)
    frontier            : Heap of nodes that we have found but have yet to explore. (Heap)
    width               : Width of the graph. (int)
    root                : Root node of the graph. (Node)
    solvable            : Whether or not the graph is solvable. (Boolean)
  Methods:
    findGoalState       : Discovers a path to the goal state using A* search. (Node)
    getDefaultGoalState : Returns the default goal state for the given id. [0,1,2,3,4,5,6,7,8...] (State)
  ----------------------------------------------------------
  """
  def __init__(self, id, heuristic = "tiles"):
    self.goalState = self.getDefaultGoalState(id)
    self.heuristic = heuristic
    self.explored = {}
    self.frontier = []
    self.expanded = 0
    heapq.heapify(self.frontier)
    
    width = math.sqrt(len(id))
    if width % 1 != 0:
      raise ValueError("Invalid id length")
    self.width = int(width)
    state = State(id, self)
    self.root = Node(None, state, self)
    self.solvable = self.root.state.calculateDisorder() % 2 == 0
  
  def findGoalState(self):
    """
    ----------------------------------------------------------
    Discovers a path to the goal state using A* search.
    Use: graph.findGoalState()
    ----------------------------------------------------------
    Asserts:
      The graph is solvable.
    Returns:
      node : Node that holds the goal state. (Node)
      -1   : The graph is not solvable.
    ----------------------------------------------------------
    """
    try:
      assert self.solvable
      node = self.root
      start = time.time()
      while(node.heuristicValue != 0): #TODO: We can prob use node.heuristicValue == 0 to check the goal state might be more effeciency
        node.expandFrontier()
        node = heapq.heappop(self.frontier)[0]
        self.explored[str(node.state)] = node

        # find if the node exists in the frontier
        # if it does, check if the new node is better
        # if it is, replace the old node with the new node
        
        #TODO: remove this later (for testing)
        if(self.expanded % 100000 == 0):
          print("Time elapsed: " + str(round(time.time() - start, 2)) + "s")
          print("Nodes Expanded: " + str(self.expanded))
          print("Current Node: "+ str(node))
          print()
      print("TOTAL NODES EXPANDED: " + str(self.expanded))
      print("TOTAL EXPLORED NODES: " + str(len(self.explored)))
      print("---------------------------------------------------------------")

      return node
    except AssertionError:
      return -1

  def getDefaultGoalState(self, id):
    """
    ----------------------------------------------------------
    Get the default goal state for the given id.
    Use: self.goalState = self.getDefaultGoalState(id)
    ----------------------------------------------------------
    """
    state = []
    for i in range(0, len(id)):
      state.append(i)
    return State(state, self)