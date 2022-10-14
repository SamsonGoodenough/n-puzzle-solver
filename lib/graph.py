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
    getDisorder         : Returns the disorder parameter of the root state. (int)
    getDefaultGoalState : Returns the default goal state for the given id. [0,1,2,3,4,5,6,7,8...] (State)
  ----------------------------------------------------------
  """
  def __init__(self, id, heuristic = "tiles"):
    self.goalState = self.getDefaultGoalState(id)
    self.heuristic = heuristic
    self.explored = {}
    self.frontier = []
    heapq.heapify(self.frontier)
    
    width = math.sqrt(len(id))
    if width % 1 != 0:
      raise ValueError("Invalid id length")
    self.width = int(width)
    state = State(id, self)
    self.root = Node(None, state, self)
    self.solvable = self.getDisorder() % 2 == 0
  
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
      count = 0
      node = self.root
      start = time.time()
      while(node.state != self.goalState): #TODO: We can prob use node.heuristicValue == 0 to check the goal state might be more effeciency
        node.expandFrontier()
        node = heapq.heappop(self.frontier)
        
        #TODO: remove this later (for testing)
        if(count % 100000 == 0):
          print("Time elapsed: " + str(round(time.time() - start, 2)) + "s")
          print("Nodes Traversed: " + str(count))
          print("Current Node: "+ str(node))
          print()
          
        count += 1
      print("---------------------------------------------------------------")
      print("TOTAL NODES TRAVERSED: " + str(count))
      return node
    except AssertionError:
      return -1
    
  #TODO: make sure graph is a valid graph (no duplicates) prob do this in getDisorder since we are already looping through the graph
  #TODO: can prob put this in the state class
  #TODO: something is up with this function idk what it is but it is not working correctly
  def getDisorder(self):
    """
    ----------------------------------------------------------
    Get the disorder of the state.
    ----------------------------------------------------------
    Returns:
      disorder: The disorder of the state.
        even  : The state is solvable.
        odd   : The state is not solvable.
        -1    : The state is the solved state.
    ----------------------------------------------------------
    """
    disorder = 0
    passFlag = False
    # pass over all the tile that matches with the goal state
    for i in range(len(self.goalState.id)-1, 0, -1):
      if not passFlag and self.goalState.id[i] == self.root.state.id[i]:
        continue
      else:
        passFlag = True
        
      # loop over remaining tiles and calculate disorder
      for j in range(i-1, -1, -1):
        if self.root.state.id[i] < self.root.state.id[j]:
          if self.root.state.id[i] == 0 or self.root.state.id[j] == 0:
            continue
          else:
            disorder += 1
    
    print("Disorder: " + str(disorder))
    if not passFlag:
      return -1 # in solved state
    else:
      return disorder

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