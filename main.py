from lib import Heuristics, Puzzle, State
from alive_progress import alive_bar
import argparse
import re

def validPuzzle(string):
  pattern = re.compile(r'^[0-9]+(,[0-9]+)*$')
  if not pattern.match(string):
    raise argparse.ArgumentTypeError("Invalid puzzle format")
  return string

parser = argparse.ArgumentParser(description='A* algorithm for n-puzzle')
parser.add_argument("-H", "--heuristic", help="The heuristic to use", choices=["manhattan", "displacement", "rowcol", "euclidean", "linear"], default="manhattan")
parser.add_argument("-s", "--size", help="The size of the puzzle e.g. 8 for 8-puzzle (3x3)", choices=[8, 15, 24, 35], type=int, default=8)
parser.add_argument("-n", "--numberOfPuzzles", help="The number of puzzles that will randomly generate.", type=int, default=100)
parser.add_argument("-o", "--outputFile", help="Supplies the file name to output text to.", default="output.txt")
parser.add_argument("-csv", "--outputCSV", help="Supplies the file name to output to csv data to.", default="stats.csv")
parser.add_argument("-d", "--debug", help="Supplies the file name to output to csv data to.", action="store_true")
parser.add_argument("-p", "--puzzle", help="Supply a puzzle for the program to solve. e.g. '-p 1,5,2,4,3,7,6,8,0'", default=None, type=validPuzzle)
args = parser.parse_args()

if(args.heuristic == "manhattan"):
  heuristic = Heuristics.MANHATTAN
elif(args.heuristic == "displacement"):
  heuristic = Heuristics.DISPLACEMENT
elif(args.heuristic == "rowcol"):
  heuristic = Heuristics.ROWCOL
elif(args.heuristic == "euclidean"):
  heuristic = Heuristics.EUCLIDEAN
elif(args.heuristic == "linear"):
  heuristic = Heuristics.LINEARCONFLICT

if(args.puzzle == None):
  puzzles = Puzzle.randomizePuzzles(heuristic, args.size, args.numberOfPuzzles)
else:
  puzzles = [State(heuristic, args.size, args.puzzle.split(","))]
if(not args.debug):
  with alive_bar(len(puzzles), enrich_print=False) as bar:
    for i in Puzzle.solvePuzzleArray(puzzles, args.outputFile, args.outputCSV):
      bar()
else:
  for i in Puzzle.solvePuzzleArray(puzzles, args.outputFile, args.outputCSV, True):
    pass
