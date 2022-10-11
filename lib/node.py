from copy import deepcopy
import heapq

from .state import State
#TODO: Check rotations of states when visiting a node
class Node:
  """
  ----------------------------------------------------------
  Node Class
  ----------------------------------------------------------
  Parameters:
      parent          : The parent node of the current node. (Node)
      children        : The children nodes of the current node. (List of Nodes)
      state           : The state of the current node. (State)
      graph           : The graph that the node is in. (Graph)
      pathCost        : The cost of the path from the start node to the current node. By default this is 0 aka root node (int)

  Variables:
      state           : The state of the node. (State)
      pathCost        : The cost of the path to the node. (int)
      heuristicValue  : The heuristic value of the node. (int)
      cost            : The cost of the node. cost = pathCost + heuristicValue (int)
      parent          : The parent node of the current node. (Node)
      graph           : The graph that the node is in. (Graph)
  
  Methods:
      ExpandFrontier  : Expands the frontier adding the nodes above, right, below, and left of the current node. (Array)
        findUp          : finds the node above the current node and returns the new node. (Node)
        findRight       : finds the node to the right of the current node and returns the new node. (Node)
        findDown        : finds the node below the current node and returns the new node. (Node)
        findLeft        : finds the node to the left of the current node and returns the new node. (Node)
      printPath       : Prints the path from the root node to the current node by going back through parent nodes. (Void)
  ----------------------------------------------------------
  """
  def __init__(self, parent, state, graph, pathCost = 0):
    self.state = state
    self.pathCost = pathCost
    
    # TODO: Based on the heuristic function, calculate the heuristic value of the node (manhattan and h3 are not implemented)
    if(graph.heuristic == "tiles"):
      self.heuristicValue = self.state.calculateMisplacedTiles()
    elif(graph.heuristic == "manhattan"):
      print("manhattan")
    elif(graph.heuristic == "h3"):
      print("h3")
      
    self.cost = self.pathCost + self.heuristicValue
    self.parent = parent
    self.graph = graph
    self.children = []
    
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
  
  def expandFrontier(self):
    """
    ----------------------------------------------------------
    Adds the nodes that are reachable from the current node to the frontier heap.
    Use: node.expandFrontier()
    ----------------------------------------------------------
    """
    node = self.findUp()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
      self.children.append(node)
    node = self.findRight()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
      self.children.append(node)
    node = self.findDown()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
      self.children.append(node)
    node = self.findLeft()
    if (node != None):
      heapq.heappush(self.graph.frontier, node)
      self.children.append(node)
    return
  
  def findUp(self):
    """
    ----------------------------------------------------------
    Finds the node above the current node and returns it.
    Use: node = findUp()
    ----------------------------------------------------------
    Returns:
      n - Node that is above the current node. (Node)
      None - If there is no node above the blank or the above node is in the explored dictionary. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if blank < self.graph.width:
      return None # can't move up
    else:
      newState.id[blank] = deepcopy(self.state.id[blank-self.graph.width]) #idk if I need this deepcopy but just in case I'm doing it anyway
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
      None - If there is no node to the right of blank or the right node is in the explored dictionary. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if (blank+1) % self.graph.width == 0:
      return None # can't move right
    else:
      newState.id[blank] = deepcopy(self.state.id[blank+1]) #idk if I need this deepcopy but just in case I'm doing it anyway
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
      None - If there is no node below blank or the below node is in the explored dictionary. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if blank >= self.graph.width*(self.graph.width-1):
      return None # can't move up
    else:
      newState.id[blank] = deepcopy(self.state.id[blank+self.graph.width]) #idk if I need this deepcopy but just in case I'm doing it anyway
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
      None - If there is no node to the left of blank or the left node is in the explored dictionary. (None)
    ----------------------------------------------------------
    """
    blank = self.state.id.index(0)
    newState = State(deepcopy(self.state.id), self.graph) # this is stupid
    if (blank) % self.graph.width == 0:
      return None # can't move left
    else:
      newState.id[blank] = deepcopy(self.state.id[blank-1]) #idk if I need this deepcopy but just in case I'm doing it anyway
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