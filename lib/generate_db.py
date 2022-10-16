import shelve
from collections import deque
from math import isqrt
from state import State


def breadth_first_search(initial_state, db=None, depth_lim=0):
    width = isqrt(len(initial_state.id))
    queue = deque()
    queue.append((initial_state, 0))
    explored = {repr(initial_state)}
    while queue:
        parent, depth = queue.popleft()
        if depth_lim and depth > depth_lim:
            break
        if db is not None:
            db[repr(parent)] = depth
        else:
            print(f"{parent!r}:{depth}")
        p_blank = parent.id.index(0)
        for child in parent.find_neighbours(width):
            if repr(child) not in explored:
                if child.id[p_blank] == '':
                    # move is counted in another db
                    queue.appendleft((child, depth))
                else:
                    # move counted in this db
                    queue.append((child, depth + 1))
                explored.add(repr(child))


if __name__ == "__main__":
    
    with shelve.open("../pattern-databases/8-01234.db", 'n') as db:
        state = State([
            0, 1, 2,
            3, 4, '',
            '','','',
            ])
        breadth_first_search(state, db)
        db.sync()
    
    with shelve.open("../pattern-databases/8-01234.db", 'n') as db:
        state = State([
            0, 1, 2,
            3, 4, '',
            '','','',
            ])
        breadth_first_search(state, db)
        db.sync()
    
    with shelve.open("../pattern-databases/8-05678.db", 'n') as db:
        state = State([
            0,'','',
            '','',5,
            6, 7, 8,
            ])
        breadth_first_search(state, db)
        db.sync()
    
    if False:
        # optionally replace two 8-puzzle databases with one
        # combined database is a perfect heuristic, but is much larger
        with shelve.open("../pattern-databases/8-full.db", 'n') as db:
            state = State([
                0, 1, 2,
                3, 4, 5,
                6, 7, 8,
                ])
            breadth_first_search(state, db)
            db.sync()
    
    
    print("Starting 15-puzzles...")

    with shelve.open("../pattern-databases/15-TL.db", 'n') as db:
        state = State([
            0, 1,'','',
            4, 5,'','',
            '','','','',
            '','','',''
            ])
        breadth_first_search(state, db)
        db.sync()
    print("Finished 1/4")
    
    with shelve.open("../pattern-databases/15-TR.db", 'n') as db:
        state = State([
            0,'', 2,3,
            '','',6,7,
            '','','','',
            '','','',''
            ])
        breadth_first_search(state, db)
        db.sync()
    print("Finished 2/4")
    
    with shelve.open("../pattern-databases/15-BL.db", 'n') as db:
        state = State([
            0,'','','',
            '','','','',
            8, 9,'','',
            12,13,'',''
            ])
        breadth_first_search(state, db)
        db.sync()
    print("Finished 3/4")

    with shelve.open("../pattern-databases/15-BR.db", 'n') as db:
        state = State([
            0,'','','',
            '','','','',
            '','',10,11,
            '','',14,15
            ])
        breadth_first_search(state, db)
        db.sync()
    print("Finished 4/4")

        
    # this is just to test we can read a db properly
    with shelve.open("../pattern-databases/8-01234.db", 'r') as db:
        state = State(['','',2,4,1,0,3,'',''])
        print(repr(state))
        cost = db.get(repr(state))
        print(f"The cost of {state!r} is: {cost}")
        print("Database has", len(db), "entries")
