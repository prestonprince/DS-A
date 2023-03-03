from collections import deque

def knight_attack(n, kr, kc, pr, pc):
    visited = set()
    visited.add((kr, kc))
    q = deque([ (kr, kc, 0) ])

    while q:
        r, c, move = q.popleft()

        if (r, c) == (pr, pc):
            return move

        positions = find_positions(r, c)
        for pos in positions:
            row, col = pos
            r_inbounds = 0 <= row < n
            c_inbounds = 0 <= col < n
            if r_inbounds and c_inbounds and pos not in visited:
                visited.add(pos)
                q.append(( row, col, move+1 ))

    return None

def find_positions(row, col):
    return [
    (row-2, col-1),
    (row-2, col+1),
    (row-1, col-2),
    (row-1, col+2),
    (row+1, col-2),
    (row+1, col+2),
    (row+2, col-1),
    (row+2, col+1)
  ]
