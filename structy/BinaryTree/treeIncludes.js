// Write a function, treeIncludes, that takes in the root of a binary tree and a target value. 
// The function should return a boolean indicating whether or not the value is contained in the tree.

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

function treeIncludes(root, target) {
    if (!root) return false
    if (root.val === target) return true
    return treeIncludes(root.right, target) || treeIncludes(root.left, target)
}

console.log(treeIncludes(a, "e")); // -> true
