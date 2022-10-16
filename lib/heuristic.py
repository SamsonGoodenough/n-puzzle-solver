from .state import State

class Heuristics:

    @staticmethod
    def h0_breadth_first_search(state):
        """
        ---------------------------------------------------------------
        A very naive (but admissible and consistent!) heuristic.
        Emulates breadth-first search.
        ---------------------------------------------------------------
        Returns:
            0 if `state` is a goal State, otherwise 1. (int)
        ---------------------------------------------------------------
        """
        for i in range(1, len(state.id)):
            if state.id[i] != i:
                # mismatch ==> non-goal state
                return 1
        # no mismatch ==> goal state
        return 0

    @staticmethod
    def h1_Hamming_distance(state, _=None): # aka misplaced tiles
        """The number of tiles in the wrong position."""
        misplaced_tiles = 0
        # skip expected blank at index 0
        for pos, tile in enumerate(state.id[1:], 1):
            if tile != pos:
                misplaced_tiles += 1
        return misplaced_tiles
    
    @staticmethod
    def h2_Manhattan_distance(state, width):
        """
        The number of moves each tile is from its position in the goal
        State, summed over every tile.
        """
        distance = 0
        for pos, tile in enumerate(state.id):
            # count tiles only, not the blank (i.e., 0)
            if tile != 0:
                distance += (abs(pos//width - tile//width)
                    + abs(pos%width - tile%width))
        return distance
    
    @staticmethod
    def h3_disjoint_pattern_datebase(state, dbs):
        if len(state.id) == 9 and len(dbs) == 1:
            # 8 puzzle: 1 database only
            return dbs[0].get(repr(state))
        elif len(state.id) == 9:
            s0 = State([i if i < 5 else '' for i in state.id])
            s1 = State([i if i > 4 or not i else '' for i in state.id])
            return dbs[0].get(repr(s0)) + dbs[1].get(repr(s1))
        elif len(state.id) == 16 and len(dbs) == 2:
            s0 = State([i if i < 9 else '' for i in state.id])
            s1 = State([i if i > 8 or not i else '' for i in state.id])
            return dbs[0].get(repr(s0)) + dbs[1].get(repr(s1))
        elif len(state.id) == 16:
            s0 = State([i if i in (0,1,4,5) else '' for i in state.id])
            s1 = State([i if i in (0,2,3,6,7) else '' for i in state.id])
            s2 = State([i if i in (0,8,9,12,13) else '' for i in state.id])
            s3 = State([i if i in (0,10,11,14,15) else '' for i in state.id])
            return (dbs[0].get(repr(s0)) + dbs[1].get(repr(s1))
                + dbs[2].get(repr(s2)) + dbs[3].get(repr(s3)))
        raise NotImplementedError(
            "Only 8-puzzles and 16-puzzles are supported"
            )
