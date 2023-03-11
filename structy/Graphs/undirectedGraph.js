// Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB). 
// The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.

function undirectedPath(edges, nodeA, nodeB) {
    const graph = buildGraph(edges);
    return hasPath(graph, nodeA, nodeB, new Set());
};

function hasPath(graph, src, dst, visited) {
    if (src === dst) return true;
    if (visited.has(src)) return false;

    visited.add(src);

    for (const neighbor of graph[src]) {
        if (hasPath(graph, neighbor, dst, visited) === true) return true
    };

    return false;
};

//! helper function to build graph
function buildGraph(edges) {
    const graph = {}

    for (const edge of edges) {
        const [a, b] = edge;

        if (!graph[a]) graph[a] = [];
        if (!graph[b]) graph[b] = [];

        graph[a].push(b)
        graph[b].push(a)
    };

    return graph
};


const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];

console.log(undirectedPath(edges, 'j', 'm')); // -> true
