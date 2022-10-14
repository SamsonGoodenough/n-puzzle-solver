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
    calculateDisorder - Calculates the disorder of the state.
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
    """
    ----------------------------------------------------------
    Description: Calculate the number of misplaced tiles in the state.
    Use: heuristicValue = state.calculateMisplacedTiles()
    ----------------------------------------------------------
    Returns:
      count - The number of misplaced tiles in the state.
    ----------------------------------------------------------
    """
    count = 0
    for i in range(len(self.id)):
      if self.id[i] != 0 and self.id[i] != self.graph.goalState.id[i]:
        count += 1 
    return count
  
  def calculateManhattanDistance(self):
    """
    ----------------------------------------------------------
    Calculate the manhattan distance of the state. (The sum of the distances of each tile from its goal position.)
    Use: heuristicValue = state.calculateManhattanDistance()
    ----------------------------------------------------------
    Returns:
      distance - the manhattn distance of the state.
    ----------------------------------------------------------
    """
    distance = 0
    for i in range(len(self.id)):
      curr_x, curr_y = self.get2DCoordinates(i)
      goal_x, goal_y = self.get2DCoordinates(self.graph.goalState.id.index(self.id[i])) # TODO: probably can just say goal_index = i since they are in order
      distance += abs(curr_x - goal_x) + abs(curr_y - goal_y)
    return distance
        
  def get2DCoordinates(self, index):
    """
    ----------------------------------------------------------
    Get the 2D coordinates of the tile at the given index.
    ----------------------------------------------------------
    Parameters:
      index: The index of the tile.
    Returns:
      x: The x coordinate of the tile.
      y: The y coordinate of the tile.
    ----------------------------------------------------------
    """
    x = index % self.graph.width
    y = index // self.graph.width
    return x, y
  
  def calculateDisorder(self):
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
    disorder = 0
    passFlag = False
    # pass over all the tile that matches with the goal state
    for i in range(len(self.graph.goalState.id)-1, 0, -1):
      if not passFlag and self.graph.goalState.id[i] == self.id[i]:
        continue
      else:
        passFlag = True
        
      # loop over remaining tiles and calculate disorder
      for j in range(i-1, -1, -1):
        if self.id[i] < self.id[j]:
          # if self.id[i] == 0 or self.id[j] == 0:
          #   continue
          # else:
          disorder += 1
    
    # print("Disorder: " + str(disorder))
    if not passFlag:
      return -1 # in solved state
    else:
      return disorder
  
  def printState(self):
    for i in range(self.graph.width):
      for j in range(self.graph.width):
        print(self.id[i*self.graph.width + j], end=" ")
      print()