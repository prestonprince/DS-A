// Write a function, pathFinder, that takes in the root of a binary tree and a target value. The function should 
// return an array representing a path to the target value. If the target value is not found in the tree, then return null.

// You may assume that the tree contains unique values.

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

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

function pathFinder(root, target) {
    if (!root) return null
    if (root.val === target) return [ root.val ]

    const leftPath = pathFinder(root.left, target)
    if (leftPath) return [ root.val, ...leftPath ]

    const rightPath = pathFinder(root.right, target)
    if (rightPath) return [ root.val, ...rightPath ]

    return null
}

console.log(pathFinder(a, 'e')); // -> [ 'a', 'b', 'e' ]
