import math, random, heapq, time
from mem_top import mem_top
import logging

class Heuristics:
  def _displacementHeuristic(state):
    """
    ----------------------------------------------------------
    Description: Calculate the number of misplaced tiles in the state.
    Use: puzzles = Puzzle.randomizePuzzle(Heuristics.MISPLACED, 8)
    ----------------------------------------------------------
    Returns:
      count - The number of misplaced tiles in the state.
    ----------------------------------------------------------
    """
    count = 0
    for i in range(state.boardLength):
      if state.board[i] != 0 and state.board[i] != i:
        count += 1 
    return count
  
  def _manhattanHeuristic(state):
    """
    ----------------------------------------------------------
    Description: Calculate the manhattan distance of the state.
    Use: puzzles = Puzzle.randomizePuzzle(Heuristics.MANHATTAN, 8)
    ----------------------------------------------------------
    Parameters:
      state - The state to calculate the manhattan distance of.
    Returns:
      h - The manhattan distance of the state.
    ----------------------------------------------------------
    """
    h = 0
    for i in range(state.boardLength):
      if state.board[i] != 0:
        x1, y1 = state._get2dCoord(i)
        x2, y2 = state._get2dCoord(state.board[i])  
        h += abs(x1 - x2) + abs(y1 - y2)
    return h
  def _outOfRowColoumnHeuristic(state):
    """
    ----------------------------------------------------------
    Description: Calculate the number of tiles out of row or coloumn.
    Use: puzzles = Puzzle.randomizePuzzle(Heuristics.ROWCOL, 8)
    ----------------------------------------------------------
    Parameters:
      state - The state to calculate the heuristic from
    Returns:
      h - The number of tiles out of row or coloumn.
    ----------------------------------------------------------
    """
    h = 0
    for i in range(state.boardLength):
      if state.board[i] != 0:
        x1, y1 = state._get2dCoord(i)
        x2, y2 = state._get2dCoord(state.board[i])  
        if x1 != x2:
          h += 1
        if y1 != y2:
          h += 1
    return h
  
  def _linearConflictHeuristic(state):
    """
    ----------------------------------------------------------
    Description: Calculate the linear conflict heuristic of the state.
    Use: puzzles = Puzzle.randomizePuzzle(Heuristics.LINEARCONFLICT, 8)
    ----------------------------------------------------------
    Parameters:
      state - The state to calculate the heuristic from
    Returns:
      h - The linear conflict heuristic of the state.
    ----------------------------------------------------------
    """
    h = 0
    for i in range(state.boardLength):
      if state.board[i] != 0:
        x1, y1 = state._get2dCoord(i)
        x2, y2 = state._get2dCoord(state.board[i]) 
        h += abs(x1 - x2) + abs(y1 - y2) 
        
        if y1 == y2: # Tile is in the same row as it's goal tile
          for j in range(state.boardLength): # Check if there is a tile in the same row that gives a linear conflict
            if state.board[j] != 0:
              x3, y3 = state._get2dCoord(j)
              x4, y4 = state._get2dCoord(state.board[j])
              if y3 == y1: # on the same row
                if(x3 < x1 and x4 >= x1): # tile is in the way
                  h += 2
                  
        if x1 == x2: # Tile is in the same coloumn as it's goal tile
          for j in range(state.boardLength): # Check if there is a tile in the same coloumn that gives a linear conflict
            if state.board[j] != 0:
              x3, y3 = state._get2dCoord(j)
              x4, y4 = state._get2dCoord(state.board[j])
              if x3 == x1: # on the same col
                if(y3 < y1 and y4 >= y1): # tile is in the way
                  h += 2
    return h
                  
  
  def _euclideanHeuristic(state):
    """
    ----------------------------------------------------------
    Description: Calculate the euclidean distance of the state.
    Use: puzzles = Puzzle.randomizePuzzle(Heuristics.EUCLIDEAN, 8)
    ----------------------------------------------------------
    Parameters:
      state - The state to calculate the euclidean distance of.
    Returns:
      h - The euclidean distance of the state.
    ----------------------------------------------------------
    """
    h = 0
    for i in range(state.boardLength):
      if state.board[i] != 0:
        x1, y1 = state._get2dCoord(i)
        x2, y2 = state._get2dCoord(state.board[i])  
        h += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return h
  
  def strToHeuristic(str):
    if (str == "DISPLACEMENT"):
      return Heuristics.DISPLACEMENT
    elif (str == "MANHATTAN"):
      return Heuristics.MANHATTAN
    elif (str == "ROWCOL"):
      return Heuristics.ROWCOL
    elif (str == "LINEARCONFLICT"):
      return Heuristics.LINEARCONFLICT
    elif (str == "EUCLIDEAN"):
      return Heuristics.EUCLIDEAN
    
  def heuristicToStr(func):
    if func == Heuristics._displacementHeuristic:
      return "DISPLACEMENT"
    elif func == Heuristics._manhattanHeuristic:
      return "MANHATTAN"
    elif func == Heuristics._outOfRowColoumnHeuristic:
      return "ROWCOL"
    elif func == Heuristics._linearConflictHeuristic:
      return "LINEARCONFLICT"
    elif func == Heuristics._euclideanHeuristic:
      return "EUCLIDEAN"
  
  DISPLACEMENT = _displacementHeuristic
  MANHATTAN = _manhattanHeuristic
  ROWCOL = _outOfRowColoumnHeuristic
  EUCLIDEAN = _euclideanHeuristic
  LINEARCONFLICT = _linearConflictHeuristic

class Puzzle:
  def __init__():
    logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
    return
  
  def randomizePuzzles(heuristic, size, numPuzzles, seed):
    """
    ----------------------------------------------------------
    Description: Randomizes 100 puzzles of the given size.
    Use: puzzles = Puzzle.randomizePuzzles(Heuristics.MANHATTAN, 8)
    ----------------------------------------------------------
    Parameters:
      heuristic - The heuristic to use for the puzzles.
      size - The size of the puzzle to randomize. Must be a perfect square.
    Returns:
      puzzles - Array of randomized puzzles.
    ----------------------------------------------------------
    """
    try:
      assert math.sqrt(size + 1) % 1 == 0
      random.seed(seed)
      puzzles = []
      while len(puzzles) < numPuzzles:
        board = [i for i in range(size+1)]
        random.shuffle(board)
        s = State(board, math.sqrt(len(board)), heuristic=heuristic)
        if (s.isSolvable()):
          puzzles.append(s)
      return puzzles
    except AssertionError:
      print("ERROR:\t Size must be a perfect square!")
      return
    
  def solvePuzzleArray(puzzles, outputFile, outputCSV, debug=False):
    """
    ----------------------------------------------------------
    Description: Solves the given puzzles and writes the results to the given file.
    Use: Puzzle.solvePuzzles(puzzles)
    ----------------------------------------------------------
    Parameters:
      puzzles - An array of puzzles to solve.
    Yields:
      count - The current number of puzzles solved.
    ----------------------------------------------------------
    """
    count = 1
    totalStats = {
      'timeTaken': 0,
      'numNodesExplored': 0,
      'numStepsToSolution': 0,
      'nodesPerSecond': 0
    }
    file = open("./output/" + outputFile, "w")
    fStats = open("./output/" + outputCSV, "w")
    fStats.write("Puzzle ID,Puzzle,Time Taken,Nodes Explored,Steps to Solution,Nodes per Second\n") # write header
    for puzzle in puzzles:
      file.write("-"*150 + "\n")
      file.write(" Puzzle # " + str(count) + " | " + str(puzzle.board) + "\n")
      file.flush()
      stats = Puzzle.solvePuzzle(puzzle, debug)
      
      # Update total stats
      totalStats["numNodesExplored"] += stats["numNodesExplored"]
      totalStats["timeTaken"] += stats["timeTaken"]
      totalStats["nodesPerSecond"] += stats["nodesPerSecond"]
      totalStats["numStepsToSolution"] += len(stats["pathToSolution"])
      
      # Write to file
      file.write("\t{:<30} ---> {:.2f}s \n".format("Time taken to complete puzzle:",stats["timeTaken"]))
      file.write("\t{:<30} ---> {} \n".format("Number of expanded nodes:",str(stats["numNodesExplored"])))
      file.write("\t{:<30} ---> {} \n".format("Number of steps to solution:",str(len(stats["pathToSolution"]))))
      file.write("\t{:<30} ---> {} \n".format("Path to Solution:",str(stats["pathToSolution"])))
      file.write("\t{:<30} ---> {:.2f} nodes/s \n".format("Nodes expanded per second:",stats["nodesPerSecond"]))
      fStats.write('%s,%s,%s,%s,%s,%s\n' % (str(count),str(stats["startingBoard"]),str(stats["timeTaken"]),str(stats["numNodesExplored"]),str(len(stats["pathToSolution"])),str(stats["nodesPerSecond"])))
      yield 
      count += 1
      file.flush()
      fStats.flush()
      
    # Write total stats to file
    file.write("\n" + "="*150 + "\n")  
    file.write(" Average Stats for {} {}-Puzzles: \n".format(len(puzzles), str(puzzles[0].boardLength-1)))
    file.write("\t{:<38} ---> {:.2f}s \n".format("Average Time taken to complete puzzle:",totalStats["timeTaken"]/len(puzzles)))
    file.write("\t{:<38} ---> {} \n".format("Average Number of expanded nodes:",str(totalStats["numNodesExplored"]/len(puzzles))))
    file.write("\t{:<38} ---> {} \n".format("Average Number of steps to solution:",str(totalStats["numStepsToSolution"]/len(puzzles))))
    file.write("\t{:<38} ---> {:.2f} nodes/s \n".format("Average Nodes expanded per second:",totalStats["nodesPerSecond"]/len(puzzles)))
    file.write("="*150 + "\n")  

    file.close()
    fStats.close()
    # print average stats
    print("="*150)  
    print(" Average Stats for {} {}-Puzzles:".format(len(puzzles), str(puzzles[0].boardLength-1)))
    print("\t{:<38} ---> {:.2f}s".format("Average Time taken to complete puzzle:",totalStats["timeTaken"]/len(puzzles)))
    print("\t{:<38} ---> {}".format("Average Number of expanded nodes:",str(totalStats["numNodesExplored"]/len(puzzles))))
    print("\t{:<38} ---> {}".format("Average Number of steps to solution:",str(totalStats["numStepsToSolution"]/len(puzzles))))
    print("\t{:<38} ---> {:.2f} nodes/s".format("Average Nodes expanded per second:",totalStats["nodesPerSecond"]/len(puzzles)))
    print("="*150)  
    
    return
    
  def solvePuzzle(s, debug=False):
    """
    ----------------------------------------------------------
    Description: Solves the given puzzle using A*.
    Use: stats = Puzzle.solvePuzzle(puzzle)
    ----------------------------------------------------------
    Parameters:
      s - Starting state to solve the puzzle from.
      debug - Whether or not to print debug information.
    Returns:
      stats - Dictionary containing the following information:
        timeTaken         - The time taken to solve the puzzle.
        numNodesExplored  - The number of nodes explored.
        pathToSolution    - The path to the solution.
        nodesPerSecond    - The number of nodes expanded per second.
    ----------------------------------------------------------
    """
    explored = {}
    frontier = []
    startingBoard = s
    start = time.time()
    heapq.heapify(frontier) # create heap and add initial state
    heapq.heappush(frontier, s._getStateAsStr())

    if debug: print('start:\t', str(s))
    while len(frontier) != 0: # loop until frontier is empty
      sParams = heapq.heappop(frontier) # (newState.f, newState.board, newState.g, newState.h, newState.path, newState.heuristicFunction)
      # print('params:\t', sParams)
      s = State.strToState(sParams[2])
      exploredCost = explored.get(str(s))
      if exploredCost != None:
        if exploredCost <= s.g: # if the explored cost is less than the current cost, then we don't need to explore this state
          continue
      explored[str(s)] = s.g
      
      if s.h == 0: # check if at the goal state
        break
      
      if debug:
        if len(explored) % 100000 == 0:
          print(mem_top())
          print('#explored:\t', len(explored))
          print('nps:\t\t {:.2f}\n'.format(len(explored) / (time.time() - start)))
        
      for move in s.getMoves(): # add all possible moves to the frontier
        heapq.heappush(frontier, move)

    # pass the solution and stats back to the caller
    end = time.time()
    stats = {
      'timeTaken': (time.time() - start),
      'numNodesExplored': len(explored),
      'pathToSolution': s.path[:],
      'nodesPerSecond': len(explored) / ((end - start) if (end - start) != 0 else 0.01),
      'startingBoard': '-'.join(str(x) for x in startingBoard.board)
    }
    if debug: 
      print('\ndone:\t', str(s)) 
      print("\t{:<30} ---> {:.2f}s ".format("Time taken to complete puzzle:",stats["timeTaken"]))
      print("\t{:<30} ---> {} ".format("Number of expanded nodes:",str(stats["numNodesExplored"])))
      print("\t{:<30} ---> {} ".format("Number of steps to solution:",str(len(stats["pathToSolution"]))))
      print("\t{:<30} ---> {} ".format("Path to Solution:",str(stats["pathToSolution"])))
      print("\t{:<30} ---> {:.2f} nodes/s ".format("Nodes expanded per second:",stats["nodesPerSecond"]))
    return stats

class State:
  def __init__(self, board, width, g=0, h=None, path = [], heuristic=Heuristics.MANHATTAN):
    self.board = board
    self.boardLength = len(board)
    self.width = width
    self.heuristicFunction = heuristic
    self.g = g
    self.h = self.getH() if h == None else h
    self.f = self.g + self.h
    self.path = path
    # print("INIT | board: {} | g: {} | h: {} | f: {} | path: {}".format(self.board, self.g, self.h, self.f, self.path))
    
  def __str__(self):
    return ','.join(map(str, self.board))
    
  def __eq__(self, other):
    return str(self) == str(other)
  def __lt__(self, other):
    return self.f < other.f
  def __le__(self, other):
    return self.f <= other.f
  def __gt__(self, other):
    return self.f > other.f
  def __ge__(self, other):
    return self.f >= other.f
  
  def getH(self):
    return self.heuristicFunction(self)
    
  def _get2dCoord(self, index):
    return (index % self.width, index // self.width)
  
  def getMoves(self):
    """
    ----------------------------------------------------------
    Description - Finds the states that are reachable from self state.
    Use: State.getMoves()
    ----------------------------------------------------------
    """
    moves = []
    # print("IN getMoves:", self.board)
    index = self.board.index(0)
    row = index // self.width
    col = index % self.width
    if row > 0:
      moves.append(self._swap(index, index - self.width))
    if row < self.width - 1:
      moves.append(self._swap(index, index + self.width))
    if col > 0:
      moves.append(self._swap(index, index - 1))
    if col < self.width - 1:
      moves.append(self._swap(index, index + 1))
    return moves
  
  def _swap(self, index1, index2):
    board = self.board[:]
    index1 = int(index1)
    index2 = int(index2)
    step = board[index2]
    board[index1], board[index2] = board[index2], board[index1]
    newState = State(board, self.width, self.g + 1, path = self.path + [step], heuristic=self.heuristicFunction)
    #f, newState.board, newState.g, newState.h, newState.path, newState.heuristicFunction
    return newState._getStateAsStr()
  
  def _getStateAsStr(self):
    return (self.f, self.h, '%s|%s|%s|%s|%s' % (State.arrayToStr(self.board), self.g, self.h, State.arrayToStr(self.path), Heuristics.heuristicToStr(self.heuristicFunction)))
  
  def arrayToStr(board):
    return ','.join(map(str, board))
    
  def strToState(str):
    boardAsStr, g, h, pathAsStr, heuristic = str.split('|') # split the string into the board, g, h, path, and heuristic
    board = list(map(int, boardAsStr.split(','))) # convert the stringified board to a list of ints
    path = list(pathAsStr.split(',')) if pathAsStr != '' else [] # convert the stringified path to a list of ints
    # print('path =================', path)
    # print("Board: ",board, "g: ",g, "h: ",h, "path: ",path, "heuristic: ",heuristic)
    return State(board, math.sqrt(len(board)), float(g), float(h), path, Heuristics.strToHeuristic(heuristic))
  
  def isSolvable(self):
    inversions = 0
    for i in range(self.boardLength):
      for j in range(i + 1, self.boardLength):
        if self.board[i] != 0 and self.board[j] != 0 and self.board[i] > self.board[j]:
          inversions += 1
    
    if self.width % 2 == 0:
      row = self.board.index(0) // self.width
      if row % 2 == 0:
        return inversions % 2 == 0
      else:
        return inversions % 2 == 1
    else:
      return inversions % 2 == 0