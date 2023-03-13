function hasCycle(graph) {
    const visited = new Set();

    for (const node in graph) {
        if (isCycle(graph, node, new Set(), visited) === true) return true;
    };

    return false;
};

function isCycle(graph, node, visiting, visited) {
    if (visited.has(node)) return false;
    if (visiting.has(node)) return true;

    visiting.add(node);

    for (const neighbor of graph[node]) {
        if (isCycle(graph, neighbor, visiting, visited,)) return true
    };

    visiting.delete(node);
    visited.add(node);
    return false;
};

console.log(hasCycle({
    a: ["b"],
    b: ["c"],
    c: ["a"],
})); // -> true
