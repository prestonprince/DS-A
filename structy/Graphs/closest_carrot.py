# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. 
# In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number 
# representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, 
# but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    visited = set([ (starting_row, starting_col) ])
    q = deque([ (starting_row, starting_col, 0) ])

    while q:
        row, col, distance = q.popleft()

        if grid[row][col] == 'C':
            return distance
        
        deltas = [ (1,0), (-1, 0), (0, 1), (0, -1) ]
        for delta in deltas:
            delta_row, delta_col = delta
            r = row + delta_row
            c = col + delta_col
            pos = (r, c)
            r_inbounds = 0 <= r < len(grid)
            c_inbounds = 0 <= c < len(grid[0])
            if r_inbounds and c_inbounds and pos not in visited and grid[r][c] != 'X':
                visited.add(pos)
                q.append((r, c, distance+1))
    return -1
    
print(closest_carrot(grid, 1, 2)) # -> 4
