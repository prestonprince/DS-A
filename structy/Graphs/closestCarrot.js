function closestCarrot(grid, startRow, startCol) {
    const visited = new Set([ startRow + ',' + startCol ]);
    const q = [[ startRow, startCol, 0 ]];

    while (q.length > 0) {
        const [ r, c, distance ] = q.shift();

        if (grid[r][c] === 'C') return distance;

        const deltas = [ [r+1, c], [r-1, c], [r, c+1], [r, c-1] ];
        for (const delta of deltas) {
            const [ deltaRow, deltaCol ] = delta;
            const rInbounds = 0 <= deltaRow && deltaRow < grid.length;
            const cInbounds = 0 <= deltaCol && deltaCol < grid[0].length;
            const pos = deltaRow + ',' + deltaCol;

            if (rInbounds && cInbounds && !visited.has(pos) && grid[deltaRow][deltaCol] !== 'X') {
                visited.add(pos);
                q.push([ deltaRow, deltaCol, distance+1 ])
            }
        }
    };

    return -1
};


const grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
  ];
  
console.log(closestCarrot(grid, 1, 2)); // -> 4
