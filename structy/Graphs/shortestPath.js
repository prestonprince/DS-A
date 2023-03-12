function shortestPath(edges, nodeA, nodeB) {
    const graph = buildGraph(edges);
    const visited = new Set([ nodeA ]);
    const q = [[ nodeA, 0 ]];

    while (q.length > 0) {
        const [ node, distance ] = q.shift();

        if (node === nodeB) return distance;

        for (const neighbor of graph[node]) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                q.push([ neighbor, distance+1 ])
            }
        }
    };

    return -1
};

function buildGraph(edges) {
    const graph = {};

    for (const edge of edges) {
        const [ a, b ] = edge;

        if (!graph[a]) graph[a] = [];
        if (!graph[b]) graph[b] = [];

        graph[a].push(b)
        graph[b].push(a)
    };

    return graph;
};

const edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
  ];
  
console.log(shortestPath(edges, 'w', 'z')); // -> 2
