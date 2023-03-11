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


function leafList(root) {
    const leaves = []
    fillLeaves(root, leaves)
    return leaves
};

function fillLeaves(root, leaves) {
    if (!root) return;
    if (!root.right && !root.left) leaves.push(root.val)
    fillLeaves(root.left, leaves)
    fillLeaves(root.right, leaves)
};

console.log(leafList(a)); // -> [ 'd', 'e', 'f' ] 
