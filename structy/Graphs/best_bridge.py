# Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). 
# There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. 
# Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]

from collections import deque

def best_bridge(grid):
    main_island = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potential_island = traverse_island(grid, r, c, set())
            if len(potential_island) > 0:
                main_island = potential_island
                break
    
    q = deque([])
    visited = set(main_island)
    for pos in main_island:
        r, c = pos
        q.append(( r, c, 0 ))
    
    while q:
        r, c, distance = q.popleft()

        if grid[r][c] == 'L' and (r, c) not in main_island:
            return distance - 1

        deltas = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_r = r + delta_row
            neighbor_c = c + delta_col
            neighbor_pos = (neighbor_r, neighbor_c)
            if neighbor_pos not in visited and is_inbounds(grid, neighbor_r, neighbor_c):
                visited.add(neighbor_pos)
                q.append(( neighbor_r, neighbor_c, distance+1 ))


def is_inbounds(grid, r, c):
    row_inbounds = 0<=r<len(grid)
    col_inbounds = 0<=c<len(grid[0])
    return row_inbounds and col_inbounds


def traverse_island(grid, r, c, visited):
    if not is_inbounds(grid, r, c) or grid[r][c] == 'W':
        return visited
    
    pos = (r, c)
    if pos in visited:
        return visited

    visited.add(pos)

    traverse_island(grid, r+1, c, visited)
    traverse_island(grid, r-1, c, visited)
    traverse_island(grid, r, c+1, visited)
    traverse_island(grid, r, c-1, visited)
    return visited

print(best_bridge(grid)) # -> 1
