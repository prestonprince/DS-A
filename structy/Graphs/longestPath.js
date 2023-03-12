function longestPath(graph) {
    const distance = {};
    for (const node in graph) {
        if (graph[node].length === 0) {
            distance[node] = 0;
        }
    };

    for (const node in graph) {
        explore(graph, node, distance);
    };

    return Math.max(...Object.values(distance))
};

function explore(graph, node, distance) {
    if (node in distance) return distance[node];

    let max = 0;
    for (const neighbor of graph[node]) {
        const size = explore(graph, neighbor, distance);
        if (size > max) max = size
    };

    distance[node] = 1 + max;
    return distance[node];
};

const graph = {
    a: ['c', 'b'],
    b: ['c'],
    c: []
  };
  
console.log(longestPath(graph)); // -> 2
