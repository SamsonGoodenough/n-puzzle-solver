import heapq
import math
from .state import State
from .node import Node

class Graph:
  """
  ----------------------------------------------------------
  Graph class
  Use: Holds the root state and goal state of the graph.
  ----------------------------------------------------------
  Parameters:
    id - ID of the root state. (String/Array idk we'll see)
  Variables:
    goalState - Goal state of the graph. By default this is in increasing order: 0,1,2,3,4,5,6,7,8... (State)
    root      - Root node of the graph. (Node)
    solvable  - Whether or not the graph is solvable. (Boolean)
  Methods:
    discover  - Discovers a path to the goal state. (Void)
    getDisorder - Returns the disorder parameter of the root state. (int)
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
  
  # depth-first search explore WILL CHANGE TO A* USING HEURISTICS
  def discover(self):
    assert self.solvable
    node = self.root
    while(node.state != self.goalState):
      node.explore()
      node = heapq.heappop(self.frontier)
    
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
  def getDisorder(self):
    disorder = 0
    passFlag = False
    # loop over all the tiles
    for i in range(len(self.goalState.id)-1, 0, -1):
      if not passFlag and self.goalState.id[i] == self.root.state.id[i]:
        continue
      else:
        passFlag = True
        
      # loop over all the tiles before the current tile
      for j in range(i-1, 0, -1):
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
    state = []
    for i in range(0, len(id)):
      state.append(i)
    return State(state, self)