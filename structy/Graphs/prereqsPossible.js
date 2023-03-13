function prereqsPossible(numCourses, prereqs) {
    const graph = buildGraph(numCourses, prereqs);
    const visited = new Set();

    for (const node in graph) {
        if (isCycle(graph, node, new Set(), visited) === true) return false;
    };

    return true;
};

function isCycle(graph, node, visiting, visited) {
    if (visited.has(node)) return false;
    if (visiting.has(node)) return true;

    visiting.add(node);

    for (const neighbor of graph[node]) {
        if (isCycle(graph, neighbor, visiting, visited) === true) return true
    };

    visiting.delete(node);
    visited.add(node);
    return false;
}

function buildGraph(numCourses, prereqs) {
    const graph = {};

    for (let i = 0; i < numCourses; i += 1) {
        graph[i] = []
    };

    for (const prereq of prereqs) {
        const [ a, b ] = prereq;

        graph[a].push(b)
    };

    return graph;
};


const numCourses = 6;
const prereqs = [
  [0, 1],
  [2, 3],
  [0, 2],
  [1, 3],
  [4, 5],
];
console.log(prereqsPossible(numCourses, prereqs)); // -> true
