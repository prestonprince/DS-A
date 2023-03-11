// Write a function, largestComponent, that takes in the adjacency list of an undirected graph. 
// The function should return the size of the largest connected component in the graph.

function largestComponent(graph) {
    if (Object.keys(graph).length === 0) return 0;

    const visited = new Set()
    let largest = -Infinity

    for (const node in graph) {
        const size = exploreSize(graph, node, visited);
        if (size > largest) largest = size;
    };

    return largest;
};

function exploreSize(graph, node, visited) {
    if (visited.has(String(node))) return 0

    visited.add(String(node));

    let size = 1
    for (const neighbor of graph[node]) {
        size += exploreSize(graph, neighbor, visited)
    };

    return size;
};

console.log(largestComponent({
    0: ['8', '1', '5'],
    1: ['0'],
    5: ['0', '8'],
    8: ['0', '5'],
    2: ['3', '4'],
    3: ['2', '4'],
    4: ['3', '2']
  })); // -> 4
