class State:
  SOLVED_STATE = "012345678"
  
  def __init__(self, id):
    self.id = id
  
  def __str__(self):
    return str(self.id)
  
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
    for i in range(len(self.SOLVED_STATE), 0, -1):
      if self.SOLVED_STATE[i] == self.id[i]:
        continue
      else:
        passFlag = True
        
      for j in range(i-1, 0, -1):
        if self.id[j] > self.id[i]:
          disorder += 1
    
    if not passFlag:
      return -1 # in solved state
    else:
      return disorder

  def printState(self):
    print(self.id[0:3])
    print(self.id[3:6])
    print(self.id[6:9])