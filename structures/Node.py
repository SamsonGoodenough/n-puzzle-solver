import State
class Node:
  def __init__(self, state, explored):
    self.state = state
    self.next = [None, None, None, None]
    self.explored = explored.push(self.state)
  
  def explore(self):
    assert self.state != None
    self.next = [Node(self.moveUp(), self), Node(self.moveRight(), self), Node(self.moveDown(), self), Node(self.moveLeft(), self)]
    return self.explored
    
  def moveUp(self):
    s = State()
    blank = self.state.id.find("0")
    if blank < 3:
      return None # can't move up
    else:
      self.id[blank] = self.state.id[blank-3]
      self.id[blank-3] = "0"
      
    return Node(s, self.explored)
  
  def moveRight(self):
    return
  
  def moveDown(self):
    return
  
  def moveLeft(self):
    return