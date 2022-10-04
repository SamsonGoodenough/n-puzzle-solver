from copy import deepcopy
import heapq

from .state import State
#TODO: Check rotations of states when visiting a node
#TODO: Remake node docstring
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
    return other != None and self.cost == other.cost
  def __str__(self):
    return "ID: "+ str(self.state.id)+ " Path-Cost: "+ str(self.pathCost) + " Heuristic-Value: " + str(self.heuristicValue) + " Cost: " + str(self.cost)
  
  def explore(self):
    #add all possible next nodes to the frontier array
    node = self.findUp()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
    node = self.findRight()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
    node = self.findDown()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
    node = self.findLeft()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
    return
  
  def findUp(self):
    """
    ----------------------------------------------------------
    Finds the node above the current node and returns it.
    Use: node = findUp()
    ----------------------------------------------------------
    Returns:
      n - Node that is above the current node. (Node)
      None - If the move is not possible or we have visited the above node. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if blank < self.graph.width:
      return None # can't move up
    else:
      newState.id[blank] = self.state.id[blank-self.graph.width]
      newState.id[blank-self.graph.width] = 0
    try:
      if (self.graph.explored[str(newState)] == True):
        return None
    except KeyError:
      n = Node(self, newState, self.graph, self.pathCost+1)
      return n
  
  def findRight(self):
    """
    ----------------------------------------------------------
    Finds the node right of the current node and returns it.
    Use: node = findRight()
    ----------------------------------------------------------
    Returns:
      n - Node that is right of the current node. (Node)
      None - If the move is not possible or we have visited the right node. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if (blank+1) % self.graph.width == 0:
      return None # can't move right
    else:
      newState.id[blank] = deepcopy(self.state.id[blank+1])
      newState.id[blank+1] = 0
    try:
      if (self.graph.explored[str(newState)] == True):
        return None
    except KeyError:
      n = Node(self, newState, self.graph, self.pathCost+1)
      return n

  
  def findDown(self):
    """
    ----------------------------------------------------------
    Finds the node below the current node and returns it.
    Use: node = findDown()
    ----------------------------------------------------------
    Returns:
      n - Node that is below the current node. (Node)
      None - If the move is not possible or we have visited the below node. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if blank >= self.graph.width*(self.graph.width-1):
      return None # can't move up
    else:
      newState.id[blank] = deepcopy(self.state.id[blank+self.graph.width])
      newState.id[blank+self.graph.width] = 0
    try:
      if (self.graph.explored[str(newState)] == True):
        return None
    except KeyError:
      n = Node(self, newState, self.graph, self.pathCost+1)
      return n
  
  def findLeft(self):
    """
    ----------------------------------------------------------
    Finds the node left of the current node and returns it.
    Use: node = findLeft()
    ----------------------------------------------------------
    Returns:
      n - Node that is left of the current node. (Node)
      None - If the move is not possible or we have visited the left node. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if (blank) % self.graph.width == 0:
      return None # can't move left
    else:
      newState.id[blank] = deepcopy(self.state.id[blank-1])
      newState.id[blank-1] = 0
    try:
      if (self.graph.explored[str(newState)] == True):
        return None
    except KeyError:
      n = Node(self, newState, self.graph, self.pathCost+1)
      return n
    
  def printPath(self):
    """
    ----------------------------------------------------------
    Prints the path from the start node to the current node.
    Use: node.printPath()
    ----------------------------------------------------------
    """
    if self.parent != None:
      self.parent.printPath()
    print(self)
    return