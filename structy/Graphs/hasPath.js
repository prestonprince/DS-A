//! dfs recursive
function hasPath(graph, src, dst) {
    if (src === dst) return true

    for (const neighbor of graph[src]) {
        if (hasPath(graph, neighbor, dst) === true) return true
    };

    return false
};

//! dfs iterative
// function hasPath(graph, src, dst) {
//     const stack = [ src ]
    
//     while (stack.length > 0) {
//         const node = stack.pop()
//         if (node === dst) return true
        
//         for (const neighbor of graph[node]) {
//             stack.push(neighbor)
//         }
//     };

//     return false
// }

//! bfs
// function hasPath(graph, src, dst) {
//     const q = [ src ];

//     while (q.length > 0) {
//         const node = q.shift()
//         if (node === dst) return true

//         for (const neighbor of graph[node]) {
//             q.push(neighbor)
//         };
//     };

//     return false
// };

const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
  };
  
console.log(hasPath(graph, 'f', 'j')); // false
