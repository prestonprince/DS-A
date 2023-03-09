// Write a function, treeLevels, that takes in the root of a binary tree. The function should return a 
// 2-Dimensional array where each subarray represents a level of the tree

const { notEqual } = require("assert");

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a       level: 0
//    /   \
//   b     c    level: 1
//  / \     \
// d   e     f  level: 2

//! iterative dfs
// function treeLevels(root) {
//     if (!root) return []
//     const stack = [{ node: root, levelNum: 0 }]
//     const levels = []

//     while (stack.length > 0) {
//         const { node, levelNum } = stack.pop()

//         if (levels.length === levelNum) {
//             levels.push([ node.val ])
//         } else {
//             levels[levelNum].push(node.val)
//         }

//         if (node.right) stack.push({ node: node.right, levelNum: levelNum + 1 })
//         if (node.left) stack.push({ node: node.left, levelNum: levelNum + 1 })
//     }

//     return levels
// }

//! recursive dfs
function treeLevels(root) {
    const levels = [];

    fillLevels(root, levels, 0)

    return levels;
};

function fillLevels(root, levels, levelNum) {
    if (!root) return;

    if (levels.length === levelNum) {
        levels.push([ root.val ])
    } else {
        levels[levelNum].push(root.val)
    };

    fillLevels(root.left, levels, levelNum+1);
    fillLevels(root.right, levels, levelNum+1);
}

console.log(treeLevels(a)); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f']
// ]
