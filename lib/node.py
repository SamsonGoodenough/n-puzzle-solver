class Node:
    """
    -------------------------------------------------------------------
    Node Class
    -------------------------------------------------------------------
    Constructor Parameters:
        parent - a node directly reachable from this node. (Node)
        state - a State object with information about the tiles (State)
        graph - the Graph this Node is in. Defaults to the graph of the
            parent. (Graph)
    Attributes:
        state - a State object with information about the tiles (State)
        depth - the (exact) minimum number of moves to get from the
            initial State to this State. (int >= 0)
        heuristic_value - a lower bound for the number of moves
            required to get from this state to a goal state. (int >= 0)
        cost - a lower bound for the total cost of a path from the
            initial State to a goal State through this node. (int >= 0)
        parent - a node directly reachable from this node. (Node)
        graph - the Graph this Node is in.. (Graph)
    Public Methods:
        print_path - prints the path from the root Node to this Node
            (by recursing through parent Nodes).
    -------------------------------------------------------------------
    """
    def __init__(self, parent, state, graph=None):
        self.parent = parent
        self.state = state
        try:
            # if parent node is non-null, use its graph
            self.depth = self.parent.depth + 1
            self.graph = self.parent.graph
        except AttributeError:
            # parent is None (i.e., self is the root node)
            self.depth = 0
            self.graph = graph
        self.heuristic_value = self.graph.heuristic(self.state, self.graph.h_param)
        self.cost = self.depth + self.heuristic_value
    
    # Nodes are prioritized by the estimate of the cheapest path to the goal
    # which which includes the node.  Specifically, f(n) = g(n) + h(n), where
    # - g(n) is the acutal number of moves required to get to this state
    # - h(n) is an estimate of the remaining moves required to reach the goal
    #
    # Break ties by preferring deeper nodes (subject to less underestimation).
    def __lt__(self, other):
        return (self.cost, self.heuristic_value) \
            < (other.cost, other.heuristic_value)
    def __le__(self, other):
        return (self.cost, self.heuristic_value) \
            <= (other.cost, other.heuristic_value)
    def __eq__(self, other):
        return other is not None \
            and (self.cost, self.heuristic_value) \
            == (other.cost, other.heuristic_value)
    
    def __str__(self):
        s = f"{self.state!s} Depth:{self.depth:02d} + " \
            f"Heuristic:{self.heuristic_value:02d} = Total:{self.cost:02d}"
        return s
    
    def __repr__(self):
        s = f"ID:{self.state!r} Depth:{self.depth:02d}, " \
            f"Heuristic:{self.heuristic_value:02d}, Total:{self.cost:02d}"
        return s
    
    def print_path(self):
        """
        ----------------------------------------------------------
        Prints the path from the start node to the current node.
        Use: node.printPath()
        ----------------------------------------------------------
        Returns: None
        ----------------------------------------------------------
        """
        if self.parent is not None:
            self.parent.print_path()
        print(self, end = "\n\n")
        return None
