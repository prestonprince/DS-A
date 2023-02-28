# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
# The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def minimum_island(grid):
    lowest = float('inf')
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, visited)
            if size != 0 and size < lowest:
                lowest = size
    return lowest


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == 'W':
        return 0
    
    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    count = 1
    count += explore(grid, r-1, c, visited)
    count += explore(grid, r+1, c, visited)
    count += explore(grid, r, c-1, visited)
    count += explore(grid, r, c+1, visited)
    return count


print(minimum_island(grid)) # -> 2
