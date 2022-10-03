import math
from .state import State
from .node import Node

def getDefaultGoalState(id):
  state = ""
  for i in range(0, len(id)):
    state += str(i)
  return State(state)

class Graph:
  def __init__(self, id):
    self.goalState = getDefaultGoalState(id)
    
    width = math.sqrt(len(id))
    if width % 1 != 0:
      raise ValueError("Invalid id length")
    
    state = State(id)
    self.root = Node(state, {}, int(width), self.goalState)
    if self.getDisorder() % 2 == 1:
      self.solvable = False
    else:
      self.solvable = True
  
  # depth-first search explore WILL CHANGE
  def discover(self):
    assert self.solvable
    self.root.explore()
    
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
        if int(self.root.state.id[i]) < int(self.root.state.id[j]):
          if self.root.state.id[i] == '0' or self.root.state.id[j] == '0':
            continue
          else:
            disorder += 1
    
    print("Disorder: " + str(disorder))
    if not passFlag:
      return -1 # in solved state
    else:
      return disorder

    