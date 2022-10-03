from .state import State

class Node:
  def __init__(self, state, explored, width, goalState):
    self.state = state
    self.next = [None, None, None, None]
    self.width = width
    self.goalState = goalState
    
    # add self to explored
    self.explored = explored
    self.explored[self.state.id] = True
    
    #sTODO REMOVE THIS
    self.state.printState()
  
  def explore(self):
    assert self.state != None
    up = self.moveUp()
    self.updateExplored(up)
    
    right = self.moveRight()
    self.updateExplored(right)
    
    down = self.moveDown()
    self.updateExplored(down)
    
    left = self.moveLeft()
    self.updateExplored(left)
    
    self.next = [up, right, down, left]
    
    return self.explored
    
  def moveUp(self):
    blank = self.state.id.find("0")
    newId = self.state.id
    if blank < self.width:
      return None # can't move up
    else:
      newId = self.strReplace(newId, blank, self.state.id[blank-self.width])
      newId[blank-self.width] = "0"
      
    if (self.explored[newId] == True):
      return None
    
    s = State(newId)
    n = Node(s, self.explored, self.width, self.goalState)
    n.explore()
    
    return n
  
  def moveRight(self):
    blank = self.state.id.find("0")
    newId = self.state.id
    if (blank+1) % self.width == 0:
      return None # can't move right
    else:
      newId[blank] = self.state.id[blank+1]
      newId[blank+1] = "0"
      
    if (self.explored[newId] == True):
      return None
    
    s = State(newId)
    n = Node(s, self.explored, self.width, self.goalState)
    n.explore()
    
    return n
  
  def moveDown(self):
    blank = self.state.id.find("0")
    newId = self.state.id
    if blank > self.width*(self.width-1):
      return None # can't move up
    else:
      newId[blank] = self.state.id[blank+self.width]
      newId[blank+self.width] = "0"
      
    if (self.explored[newId] == True):
      return None
    
    s = State(newId)
    n = Node(s, self.explored, self.width, self.goalState)
    n.explore()
    
    return n
  
  def moveLeft(self):
    blank = self.state.id.find("0")
    newId = self.state.id
    if (blank) % self.width == 0:
      return None # can't move left
    else:
      newId[blank] = self.state.id[blank-1]
      newId[blank-1] = "0"
      
    if (self.explored[newId] == True):
      return None
    
    s = State(newId)
    n = Node(s, self.explored, self.width, self.goalState)
    n.explore()
    
    return n
  
  def updateExplored(self, node):
    if node != None:
      self.explored = node.explored
    return
  
  def checkIfGoalState(self):
    return self.state.id == self.goalState.id
  
  def strReplace(str, index, char):
    return str[0:index] + char + str[index+1:]