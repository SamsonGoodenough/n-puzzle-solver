import math
import random
class Heuristics:
  def _displacementHeuristic(state):
    pass
  
  def _manhattanHeuristic(state):
    h = 0
    for i in range(state.boardLength):
      if state.board[i] != 0:
        x1, y1 = state._get2dCoord(i)
        x2, y2 = state._get2dCoord(state.board[i])
        h += abs(x1 - x2) + abs(y1 - y2)
    return h
  
  DISPLACEMENT = _displacementHeuristic
  MANHATTAN = _manhattanHeuristic
  
  

class State:
  def __init__(self, board, width, g=0, path = [], heuristic=Heuristics.MANHATTAN):
    self.board = board
    self.boardLength = len(board)
    self.width = width
    self.heuristicFunction = heuristic
    self.g = g
    self.h = self.getH()
    self.f = self.g + self.h
    self.path = path
    
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
    moves = []
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
    return State(board, self.width, self.g + 1, self.path + [step], heuristic=self.heuristicFunction)
  
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