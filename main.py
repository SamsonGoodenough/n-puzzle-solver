from random import sample
from array import array
from lib.graph import Graph
from lib.heuristic import Heuristics
from lib.state import State


def random_board(n):
    """
    -------------------------------------------------------------------
    Generates a random puzzle.  puzzle is guaranteed to be valid (i.e.,
    have each number exactly once), but is not guaranteed to be
    solveable.
    Use: board = random_puzzle(n)
    -------------------------------------------------------------------
    Paremeters:
        n - the number of positions in the board.  Must be a perfect
            square. (int > 0)
    Returns:
        puzzle - an array containing each digit in [0,n) in a random
            order. (array)
    -------------------------------------------------------------------
    """
    # array uses less memory than list by requiring all elements to be
    # of the same type (in this case, 8-bit unsigned integers)
    board = array('B', sample(range(n), n))
    return board


def effective_branching_factor(d, n, err=1e-7):
    """Computes effective branching factor using bisection method"""
    low = 1
    high = pow(n, 1.0 / d) + 1
    mid = (low + high) / 2
    while high - low > err: 
        estimate = sum(pow(mid, i) for i in range(1, d+1))
        if estimate > n:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid


if __name__ == "__main__":

    # short-circuit: use `or` for TEST, `and` for REPORT
    MODE = "TEST" or "REPORT"

    if MODE == "TEST": # testing / hardcoded inputs / debugging / etc.

        # `3 or` short circuits (get rid of it if you want to be prompted)
        h = 1 or int(input("Heuristic:\n" \
            " -1) BFS\n" \
            "  1) Hamming distance / misplaced tiles (h1)\n" \
            "  2) Manhattan distance (h2, default)\n" \
            "  3) (discrete) pattern databases (h3)\n"))

        if h < 1:
            heuristic = Heuristics.h0_breadth_first_search
        elif h == 1:
            heuristic = Heuristics.h1_Hamming_distance
        elif h == 2:
            heuristic = Heuristics.h2_Manhattan_distance
        else:
            heuristic = Heuristics.h3_disjoint_pattern_datebase
        
        # `4 or` short circuits (get rid of it if you want to be prompted
        mode = 1 or int(input("Mode:\n" \
            "  1) hardcoded\n" \
            "  3) random (solvable) 8-puzzle\n" \
            "  4) random (solvable) 15-puzzle\n" \
            "  5) random (solvable) 24-puzzle" \
            ))

        if mode not in range(3, 6):
            graph = Graph(array('B', [12,8,4,7,9,14,3,1,5,10,2,11,6,0,13,15]), heuristic) # 36
            print(graph.root.state)
        else:
            print(f"Solving a random {mode**2-1}-puzzle")
            graph = None
            while not graph or not graph.solvable:
                graph = Graph(random_board(mode ** 2), heuristic)
        
        try:
            node = graph.solve()
            print("------------------PRINTING PATH TO GOAL STATE------------------")
            graph.goal.print_path()
            print("Program terminated with:")
        except KeyboardInterrupt:
            print("\nUser terminated program with:")
        finally:
            print(f" - {len(graph.generated):,d} states discovered")
            print(f"   - {len(graph.generated)-len(graph.frontier):,d} states expanded")
            print(f"   - {len(graph.frontier):,d} states left in the frontier")
            if graph.goal:
                print(f" - the cost of an optimal solution is exactly {graph.goal.cost}")
            elif graph.frontier:
                print(f" - the cost of an optimal solution is no less than {graph.frontier[0].cost}")
            print(f" - the cost of the initial state was estimated to be {graph.root.cost}", end="")
            if graph.goal:
                print(f" ({graph.root.cost/graph.goal.cost:.1%} of actual cost)")
            if graph.frontier:
                print(f" ({graph.root.cost/graph.frontier[0].cost:.1%} of actual cost)")
            del graph # close db connections
    
    ##########################################################################
    else: # only code below this line should be kept in the final submission
        PUZZLE_COUNT = 100
        HEURISTICS = (Heuristics.h1_Hamming_distance,
                      Heuristics.h2_Manhattan_distance,
                      Heuristics.h3_disjoint_pattern_datebase,
                      )
        with open("puzzles.txt", "w") as f:
            pass # empties the file
        for n in range(3, 4): # ignore 24-puzzle for now...
            puzzles = []
            while len(puzzles) < PUZZLE_COUNT:
                new_puzzle = random_board(n**2)
                if State(new_puzzle).is_solvable(n):
                    puzzles.append(new_puzzle)
            print(f"\nGenerated {PUZZLE_COUNT} solvable {n*n-1}-puzzles...\n")
            with open("puzzles.txt", 'a') as f:
                for pi, puzzle in enumerate(puzzles, 1):
                    print(f"p{pi} : {State(puzzle)!r}", file=f)
            for hi, heuristic in enumerate(HEURISTICS, 1):
                for pi, puzzle in enumerate(puzzles, 1):
                    graph = Graph(puzzle, heuristic)
                    generated, expand, cost = graph.solve()
                    del graph # close db connections
                    bf = effective_branching_factor(cost, generated)
                    print(f"h{hi},p{pi},{generated},{expand},{cost},{bf:.4f}")
