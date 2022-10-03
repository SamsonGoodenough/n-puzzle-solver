class State:
  def __init__(self, id):
    self.id = id
  
  def __str__(self):
    return str(self.id)
    
  def printState(self):
    print(self.id[0:3])
    print(self.id[3:6])
    print(self.id[6:9])