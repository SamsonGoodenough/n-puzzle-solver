from lib import Heuristics, Puzzle
from alive_progress import alive_bar
import argparse

parser = argparse.ArgumentParser(description='A* algorithm for n-puzzle')
parser.add_argument("-H", "--heuristic", help="The heuristic to use", choices=["manhattan", "displacement"], default="manhattan")
parser.add_argument("-s", "--size", help="The size of the puzzle e.g. 8 for 8-puzzle (3x3)", choices=[8, 15, 24, 35], type=int, default=8)
parser.add_argument("-o", "--outputFile", help="Supplies the file name to output text to.", default="output.txt")
parser.add_argument("-csv", "--outputCSV", help="Supplies the file name to output to csv data to.", default="stats.csv")
parser.add_argument("-d", "--debug", help="Supplies the file name to output to csv data to.", action="store_true")
args = parser.parse_args()

if(args.heuristic == "manhattan"):
  heuristic = Heuristics.MANHATTAN
elif(args.heuristic == "displacement"):
  heuristic = Heuristics.DISPLACEMENT
  
# elif(args.heuristic == "linearConflict"): #TODO you should make yourself NOW!
  # heuristic = Heuristics.linearConflict
  
puzzles = Puzzle.randomizePuzzles(heuristic, args.size)

if(not args.debug):
  with alive_bar(100, enrich_print=False) as bar:
    for i in Puzzle.solvePuzzleArray(puzzles, args.outputFile, args.outputCSV):
      bar()
else:
  for i in Puzzle.solvePuzzleArray(puzzles, args.outputFile, args.outputCSV, True):
    pass
