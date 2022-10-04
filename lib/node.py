import heapq

from .state import State
#TODO: Check rotations of states when visiting a node
class Node:
  """
  ----------------------------------------------------------
  Node Class
  ----------------------------------------------------------
  Parameters:
      state     : The state of the node. (State)
      explored  : Array of explored nodes. (Array of Nodes)
      width     : width of the puzzle. 3 or 8-puzzle, 4 for 15-puzzle (int)
      goalState : Goal state. (state)

  Variables:
      next      : Array of the four possible next nodes. Will be None if the move is not possible, initially all directions are None. (Array of nodes)
      cost      : Cost of the node. This will be num of nodes traveled + heuristic value of state (int)
      parent    : Parent node. (Node)
  
  Methods:
      explore   : Explores the node and returns the explored array. (Array)
        moveUp    : Moves the node up and returns the new node. (Node)
        moveRight : Moves the node right and returns the new node. (Node)
        moveDown  : Moves the node down and returns the new node. (Node)
        moveLeft  : Moves the node left and returns the new node. (Node)
      checkIfGoalState : Checks if the node is the goal state. (bool)
      UpdateExplored   : Updates the explored array. (void)
      strReplace       : Helper function that replaces a character in a string. (String)
  ----------------------------------------------------------
  """
  def __init__(self, parent, state, graph, pathCost = 0):
    self.state = state
    self.pathCost = pathCost
    if(graph.heuristic == "tiles"):
      self.heuristicValue = self.state.calculateMisplacedTiles()
    self.cost = self.pathCost + self.heuristicValue
    self.parent = parent
    self.graph = graph
    
    # add self to explored
    self.graph.explored[str(self.state)] = True
  
  def __lt__(self, other):
    return self.cost < other.cost
  def __le__(self, other):
    return self.cost <= other.cost
  def __eq__(self, other):
    return self.cost == other.cost
  def __str__(self):
    return "[ID: ", self.state.id, "Cost: ", self.cost,"]"
  
  #TODO: Using heuristic function, find the next best node to explore.
  #     Add global array of frontier nodes, and add all nodes still left to traverse to the array.
  def explore(self):
    #add all possible next nodes to the frontier array
    node = self.findUp()
    if (node != None and self.graph.explored[node.state] == False):
      heapq.heappush(self.graph.frontier, node)
    node = self.findRight()
    if (node != None and self.graph.explored[node.state] == False):
      heapq.heappush(self.graph.frontier, node)
    node = self.findDown()
    if (node != None and self.graph.explored[node.state] == False):
      heapq.heappush(self.graph.frontier, node)
    node = self.findLeft()
    if (node != None and self.graph.explored[node.state] == False):
      heapq.heappush(self.graph.frontier, node)
    return
  
  def findUp(self):
    blank = self.state.id.index(0)
    newState = self.state
    if blank < self.graph.width:
      return None # can't move up
    else:
      newState[blank] = self.state.id[blank-self.graph.width]
      newState[blank-self.graph.width] = 0
    if (self.graph.explored[str(newState)] == True):
      return None
    
    s = State(newState, self.graph)
    n = Node(self, s, self.graph, self.pathCost+1)
    
    return n
  
  def findRight(self):
    blank = self.state.id.index(0)
    newId = self.state.id
    if (blank+1) % self.graph.width == 0:
      return None # can't move right
    else:
      newId[blank] = self.state.id[blank+1]
      newId[blank+1] = 0
      
    if (self.graph.explored[str(newId)] == True):
      return None
    
    s = State(newId, self.graph)
    n = Node(self, s, self.graph, self.pathCost+1)
    
    return n
  
  def findDown(self):
    blank = self.state.id.index(0)
    newId = self.state.id
    if blank > self.graph.width*(self.graph.width-1):
      return None # can't move up
    else:
      newId[blank] = self.state.id[blank+self.graph.width]
      newId[blank+self.graph.width] = 0
      
    if (self.graph.explored[str(newId)] == True):
      return None
    
    s = State(newId, self.graph)
    n = Node(self, s, self.graph, self.pathCost+1)
    
    return n
  
  def findLeft(self):
    blank = self.state.id.index(0)
    newId = self.state.id
    if (blank) % self.graph.width == 0:
      return None # can't move left
    else:
      newId[blank] = self.state.id[blank-1]
      newId[blank-1] = 0
      
    if (self.graph.explored[str(newId)] == True):
      return None
    
    s = State(newId, self.graph)
    n = Node(self, s, self.graph, self.pathCost+1)
    
    return n