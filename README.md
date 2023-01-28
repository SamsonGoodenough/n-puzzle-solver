# n-puzzle-solver

## Purpose
Tool that can solve random or given n-puzzles (n=8, 15, 24...) using the **A\* search algorithm** and return stats on the solutions.

## Heuristics
- Displacement
- Manhattan Distance
- Out Of Row Coloumn
- Linear Conflict
- Euclidean

## Usage
1. Download and install [python](https://www.python.org/downloads/)
2. Clone the repo
3. Run `pip -r requirements.txt`
4. Run `python ./main.py [-OPTIONS]`

### Options
`-n NUMBEROFPUZZLES`, `--numberOfPuzzles NUMBEROFPUZZLES`
  - The number of puzzles that will randomly generate.

`-S SEED`, `--seed SEED`
  - The seed for the random number generator

`-o OUTPUTFILE`, `--outputFile OUTPUTFILE`
  - Supplies the file name to output text to.

`-csv OUTPUTCSV`, `--outputCSV OUTPUTCSV`
  - Supplies the file name to output to csv data to.

`-d, --debug`
  - Tells the program to output debug information

`-p PUZZLE`, `--puzzle PUZZLE`
  - Supply a puzzle for the program to solve. e.g. `-p 1,5,2,4,3,7,6,8,0`

## License
MIT © License can be found [here](https://github.com/SamsonGoodenough/n-puzzle-solver/blob/main/LICENSE).
