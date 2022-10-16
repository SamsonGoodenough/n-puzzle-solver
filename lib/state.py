from math import ceil, isqrt, log10

class State:
    """
    -------------------------------------------------------------------
    Holds the position of each tile in the puzzle.
      * Informally, this class should have everything specific to
        specific to the 8-, 15-, and 24-puzzle problems, besides
        the heuristics.
    -------------------------------------------------------------------
    Constructor Parameters:
        id - a permutation of the tiles. (array of int)
          * 0 denotes the blank
          * must include every integer in 0,1,2,...,len(id)-1
          * must be flattened to a 1D array (e.g., [0,1,2,3,4,5,6,7,8]
            rather than [[0,1,2], [3,4,5], [7,8,9]])
    Public Methods:
        find_neighbours - generates a list of States that are exactly
            one move away from this State. (list of State)
        compute_disorder - computes the disorder parameter (i.e.,
            number of inversions of tiles). (int >= 0)
        is_solvable - determines whether or not this State is valid and
            solvable. (bool)
    -------------------------------------------------------------------
    """
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        '''
        Returns: a human-readable string which represents the State id (str)
        - the blank is marked with '*' (8-puzzle) or '**' (15- and 24-puzzle)
        - the string has 1 line for every row
        Example:
            * 1 2
            3 4 5
            6 7 8
        '''
        # number of rows and columns
        w = isqrt(len(self.id))
        # number of characters to print a tile
        c = ceil(log10(len(self.id)))
        s = "\n".join((
            ' '.join(f'{v:{c}d}' if v else '*'*c for v in self.id[i : i + w])
                for i in range(0, len(self.id), w)))
        return s
    
    def __repr__(self): # old __str__ method (1 line)
        '''
        Returns: a string which uniquely identifies the state
            - the blank is marked with '0'
            - the string has no newline characters
        Example: 0,1,2,3,4,5,6,7,8
        '''
        return ','.join(map(str, self.id))
    
    def __eq__(self, other):
        return self.id == other.id

    def find_neighbours(self, width):
        """
        ---------------------------------------------------------------
        Generates a list of all States that are exactly one move away.
        Use: neighbour_states = state.find_neighbours()
        ---------------------------------------------------------------
        Parameters:
            width - number of rows and columns in this State. (int > 0)
        Returns:
            neighbour_states - a list of states exactly one move away
                from this State. (list of State)
        ---------------------------------------------------------------
        """
        # current position of the blank "piece"
        blank_index = self.id.index(0)
        # to hold the indices where the blank can move to
        indices = []
        if blank_index >= width:
            # blank not in top row ==> blank can move up
            indices.append(blank_index - width)
        if blank_index + width < len(self.id):
            # blank not in bottom row ==> blank can move down
            indices.append(blank_index + width)
        if blank_index % width != 0:
            # blank not in leftmost column ==> blank can move left
            indices.append(blank_index - 1)
        if (blank_index + 1) % width != 0:
            # blank not in rightmost column ==> blank can move right
            indices.append(blank_index + 1)
        
        # generate a list of State objects using the foregoing indices
        neighbour_states = []
        for i in indices:
            new_state = State(self.id[:]) # shallow copy
            new_state.id[blank_index] = self.id[i]
            new_state.id[i] = 0
            neighbour_states.append(new_state)
        return neighbour_states
    
    def compute_disorder(self):
        """
        ---------------------------------------------------------------
        Computes the disorder parameter for this board.
        Use: disorder = state.compute_disorder()
        ---------------------------------------------------------------
        Parameters: None
        Returns:
            disorder - the number of inversions in an array of the
                tiles. Does not count the blank. (int >= 0)
        ---------------------------------------------------------------
        """
        disorder = 0
        # loop through every distinct pair of values
        for i in range(len(self.id) - 1):
            for j in range(i + 1, len(self.id)):
                # ignore the blank (i.e., 0)
                if self.id[i] != 0 and self.id[j] != 0 \
                        and self.id[i] > self.id[j]:
                    disorder += 1
        return disorder

    def is_solvable(self, width):
        """
        ---------------------------------------------------------------
        Determines whether or not the board (id) is valid and solvable.
        An id is valid iff it contains every integer in [0,len(id)-1]
        exactly once. Uses the disorder paramater (Dp) and the row of
        the blank tile to determine if a valid board is solvable.
        Use: state.is_solvable()
        ---------------------------------------------------------------
        Parameters:
            width - the number of row, columns in this State. (int > 0)
        Returns:
            solvable - True if the board is valid and solvable, False
                otherwise. (bool)
        ---------------------------------------------------------------
        """
        disorder = self.compute_disorder()
        solvable = True
        if sorted(self.id) != list(range(len(self.id))):
            # ID must contain every number in [0, len(...)] exactly once
            solvable = False
        elif width & 1 == 1 and disorder & 1 == 1:
            # 8- or 24-puzzle with ODD disorder parameter
            solvable = False
        elif width & 1 == 0:
            # 15-puzzle ==> need to check row of blank
            row = self.id.index(0) // width
            if disorder+row & 1 == 1:
                # 15-puzzle where Dp and row have different parity
                solvable = False
        return solvable
