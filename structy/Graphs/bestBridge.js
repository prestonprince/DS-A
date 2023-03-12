function bestBridge(grid) {
    let mainIsland;
    for (let r = 0; r < grid.length; r+=1) {
        for (let c = 0; c < grid[0].length; c+=1) {
            const possibleIsland = traverseIsland(grid, r, c, new Set());
            if (possibleIsland.size > 0) mainIsland = possibleIsland
        };
    };

    const visited = new Set(mainIsland);
    const q = [];
    for (const pos of mainIsland) {
        const [ row, col ] = pos.split(',').map(Number);
        q.push([ row, col, 0 ])
    };

    while (q.length > 0) {
        const [ r, c, distance ] = q.shift();

        const pos = r + ',' + c;
        if (grid[r][c] === 'L' && !mainIsland.has(pos)) {
            return distance - 1;
        };

        const deltas = [ [r+1, c], [r-1, c], [r, c+1], [r, c-1] ];
        for (const delta of deltas) {
            const [ deltaRow, deltaCol ] = delta;
            const deltaPos = deltaRow + ',' + deltaCol;

            if (!visited.has(deltaPos) && isInbounds(grid, deltaRow, deltaCol)) {
                visited.add(deltaPos);
                q.push([ deltaRow, deltaCol, distance+1 ])
            }
        }
    }
};

function isInbounds(grid, r, c) {
    rowInbounds = 0 <= r && r < grid.length
    colInbounds = 0 <= c && c < grid[0].length
    return rowInbounds && colInbounds
  }

function traverseIsland(grid, r, c, visited) {
    if (!isInbounds(grid, r, c) || grid[r][c] === 'W') return visited;
    
    const pos = r + ',' + c;
    if (visited.has(pos)) return visited;
    visited.add(pos)

    traverseIsland(grid, r+1, c, visited)
    traverseIsland(grid, r-1, c, visited)
    traverseIsland(grid, r, c+1, visited)
    traverseIsland(grid, r, c-1, visited);
    return visited;
};



const grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
  ];
console.log(bestBridge(grid)); // -> 1
