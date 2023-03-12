function semestersRequired(numCourses, prereqs) {
    const graph = buildGraph(numCourses, prereqs);
    const distance = {};

    for (let i = 0; i < numCourses; i+=1) {
        if (graph[i].length === 0) distance[i] = 1
    };

    for (let i = 0; i < numCourses; i+=1) {
        fillDistance(graph, i, distance);
    };

    return Math.max(...Object.values(distance))
};

function fillDistance(graph, node, distance) {
    if (node in distance) return distance[node];

    let max = 0;
    for (const neighbor of graph[node]) {
        const size = fillDistance(graph, neighbor, distance);
        if (size > max) max = size;
    };

    distance[node] = 1 + max;
    return distance[node]
};

function buildGraph(numCourses, prereqs) {
    const graph = {};

    for (let i = 0; i < numCourses; i+=1) {
        graph[i] = [];
    };

    for (const prereq of prereqs) {
        const [ a, b ] = prereq;
        graph[a].push(b)
    };

    return graph;
};

const numCourses = 6;
const prereqs = [
  [1, 2],
  [2, 4],
  [3, 5],
  [0, 5],
];
console.log(semestersRequired(numCourses, prereqs)); // -> 3
