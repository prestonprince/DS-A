// Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. 
// The function should return the number of connected components within the graph.

function connectedComponentsCount(graph) {
    let count = 0;
    const visited = new Set();

    for (const node in graph) {
        if (explore(graph, node, visited) === true) {
            count += 1
        };
    };

    return count
};

function explore(graph, node, visited) {
    if (visited.has(String(node))) return false;
    visited.add(String(node));

    for (const neighbor of graph[node]) {
        explore(graph, neighbor, visited);
    };

    return true;
};


console.log(connectedComponentsCount({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
  })); // -> 2
