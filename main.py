from lib import State, Heuristics
import heapq
import math
import random
import time

start = time.time()

startingBoard = [i for i in range(9)]
# startingBoard = [1, 2, 0, 3, 4, 5, 6, 7, 8]
# startingBoard = [i for i in range(16)]
# startingBoard = [4, 1, 2, 3, 5, 6, 7, 11, 8, 9, 10, 0, 12, 13, 14, 15]
random.shuffle(startingBoard)
s = State(startingBoard, math.sqrt(len(startingBoard)), heuristic=Heuristics.MANHATTAN)
while s.isSolvable() == False:
  random.shuffle(startingBoard)
  s = State(startingBoard, math.sqrt(len(startingBoard)), heuristic=Heuristics.MANHATTAN)
  
explored = {}
frontier = []
heapq.heapify(frontier)
heapq.heappush(frontier, s)

print('start:\t', str(s))
while len(frontier) != 0:
  s = heapq.heappop(frontier)
  if explored.get(str(s)) != None:
    continue
  explored[str(s)] = True
  
  if s.h == 0:
    break
  
  if len(explored) % 100000 == 0:
    print('#explored:\t', len(explored))
    print('nps:\t\t {:.2f}\n'.format(len(explored) / (time.time() - start)))
    
  
  for move in s.getMoves():
    if str(move) not in explored:
      heapq.heappush(frontier, move)

print('done:\t', str(s))
print('#explored:', len(explored))
print('#path:', '->'.join(map(str, s.path)))
print('nps:\t\t {:.2f}'.format(len(explored) / (time.time() - start)))
print('total time:\t {:.2f}\n'.format((time.time() - start)))