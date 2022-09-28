class Graph:
  def __init__(self, root):
    self.root = root
    self.visited = [self.root.state] # list of States
    if self.root.state.getDisorder() % 2 == 1:
      self.solvable = False
    else:
      self.solvable = True
  
  # depth-first search explore WILL CHANGE
  def discover(self):
    assert self.solvable
    self.appendWithoutNone(self.root.explore())
    
  def appendWithoutNone(self, stateList):
    for state in stateList:
      if state != None:
        self.visited.append(state)