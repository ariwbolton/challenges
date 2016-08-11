import itertools

field = """O O O O X O O O O O
X X O O O O O O X O
O O O O O O O O O O
O O O O O O O O O O
O O O O O X O O O O"""

field = [row.split(" ") for row in field.split("\n")]

N = len(field)
M = len(field[0])

def getNeighbors(row, col):
    rows = range(max(0, row - 1), min(N - 1, row + 1) + 1)
    cols = range(max(0, col - 1), min(M - 1, col + 1) + 1)
    
    t = (row, col)
    
    r = list(itertools.product(rows, cols))
    r.remove(t)
    return r

def getNumMines(neighbors):
    n = 0
    
    for neighbor in neighbors:
        if field[neighbor[0]][neighbor[1]] == "X":
            n += 1
            
    return str(n)

    
for row in range(0, N):
    for col in range(0, M):
        if field[row][col] == "X":
            continue
        
        neighbors = getNeighbors(row, col)
        
        field[row][col] = getNumMines(neighbors)


field = "\n".join([" ".join(row) for row in field])
print field
    
