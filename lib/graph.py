import shelve
import os
from math import sqrt
from heapq import heappush, heappop
from lib.heuristic import Heuristics
from .node import Node
from .state import State

class Graph:
    """
    -------------------------------------------------------------------
    Contains everything needed for A* search.
      * Only minor changes should be required (notably proper support
        for weighted edges) if this code were used for another A*
        implementation.
    -------------------------------------------------------------------
    Parameters:
        id - ID of the root state. (array)
        heuristic - An admissible heuristic function used to estimate
            the cost from a State to the goal. (function)
    Attributes:
        heuristic - An admissible heuristic function used to estimate
            the cost from a State to the goal. (function)
        h_param - a parameter to be passed to the heuristic function.
            e.g., a database connection, the width of a Graph. (varies)
        root - Root node of the graph (every other Node is a
            descendant of root). Holds the initial state. (Node)
        width - Width of the graph (specifically, n for an n*n-1
            puzzle). Must be a perfect square. (int > 0)
        frontier - Minimum-heap of nodes ready to be explored.
            Priority is determined by the depth and heuristic of each
            node. (list / heapq)
        generated - Set of states that have been added to the
            frontier, including any states that have since been removed
            fron the frontier. (set)
        solvable - Whether or not the graph's initial state is
            solvable. (bool)
        goal - A Node whose State is a goal State. Must be a descendant
            of root. Defaults to None until such a node is found.
            (Node)
    Public Methods:
        solve - Uses A* algorithm to find an optimal path to the goal
            State. Returns statistics used to evaluate the heuristics.
            (int, int, int)
    -------------------------------------------------------------------
    """

    def __init__(self, initial_id, heuristic):
        width = sqrt(len(initial_id))
        if not width.is_integer():
            raise ValueError("the number of positions in the initial state " \
                f"must be a perfect square, not {len(initial_id)}"
                )
        self.width = int(width)

        if not callable(heuristic):
            raise TypeError(
                f"heuristic must be a function, not {type(heuristic)}"
                )
        self.heuristic = heuristic
        if self.heuristic is Heuristics.h3_disjoint_pattern_datebase:
            # open databases
            paths = ()
            if self.width == 3:
                #paths = ("8-full.db",) # perfect heuristic
                paths = ("8-01234.db", "8-05678.db") # disjoint
            elif self.width == 4:
                paths = ("15-TL.db", "15-TR.db", "15-BL.db", "15-BR.db")
            # open each database once
            self.h_param = [shelve.open(
                os.path.join('.', 'pattern-databases', p), 'r') for p in paths
                ]
        else:
            # pass the width
            self.h_param = self.width

        self.root = Node(None, State(initial_id), graph=self)
        self.solvable = self.root.state.is_solvable(self.width)
        self.generated = {hash(self.root.state)}
        self.frontier = [self.root]
        self.goal = None # replaced with a Node if/when it is found
    
    def __del__(self):
        if self.heuristic is Heuristics.h3_disjoint_pattern_datebase:
            # close connection to each database
            for db in self.h_param:
                db.close()
    
    def solve(self):
        """
        ---------------------------------------------------------------
        Discovers a path to the goal state using A* search.
        Use: generated, expanded, cost = graph.solve()
        ---------------------------------------------------------------
        Asserts:
            The graph is solvable.
        Parameters:
            None
        Returns:
            generated - the number of distinct States generated
                during the search (int > 0)
            expanded - the number of nodes extracted from the frontier
                through the duration of the search (int > 0)
            cost - the minimum number of moves required to get from the
                initial state to a goal state (int >= 0)
        ---------------------------------------------------------------
        """
        assert self.solvable, "cannot search a graph that is unsolveable"
        node = heappop(self.frontier)
        while node.heuristic_value != 0:
            new_states = node.state.find_neighbours(self.width)
            for state in new_states:
                new_node = Node(node, state)
                self._insert(new_node)
            node = heappop(self.frontier)
        # generate statistics for comparison / report
        self.goal = node
        generated = len(self.generated)
        expanded = generated - len(self.frontier)
        cost = self.goal.cost
        return generated, expanded, cost
    
    def _insert(self, node):
        """Insert `node` if and only if it is not a duplicate"""
        # keep track of the size of the set (to check for duplicates)
        old_len = len(self.generated)
        self.generated.add(hash(node.state))
        if old_len != len(self.generated):
            # node yet to be explored ==> add it to the frontier
            heappush(self.frontier, node)
