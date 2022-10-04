class State:
  """
  ----------------------------------------------------------
  State class
  Use: Holds the state of the puzzle at a given node. Used to easily display the graph using plotly. (I think)
  ----------------------------------------------------------
  Parameters:
    id - ID of the state. (Array)
    graph - Graph that the state is a part of. (Graph)
  Methods:
    printState - Prints the state to the console.
    calculateMisplacedTiles - Calculates the number of misplaced tiles in the state.
    calculateManhattanDistance - Calculates the manhattan distance of the state.
  ----------------------------------------------------------
  """
  def __init__(self, id, graph):
    self.id = id
    self.graph = graph
  
  def __str__(self):
    return ','.join(map(str, self.id))
  
  def __eq__(self, other):
    return self.id == other.id
  
  def calculateMisplacedTiles(self):
    count = 0
    for i in range(len(self.id)):
      if self.id[i] != 0 and self.id[i] != self.graph.goalState.id[i]:
        count += 1 
    return count
  
  def calculateManhattanDistance(self):
    #TODO: calculate manhattan distance
    return
  
  def printState(self):
    for i in range(self.graph.width):
      for j in range(self.graph.width):
        print(self.id[i*self.graph.width + j], end=" ")
      print()