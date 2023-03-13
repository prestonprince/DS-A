function levelAverages(root) {
    const levels = [];
    fillLevels(root, levels, 0);
    const averages = levels.map(level =>
        average(level));

    return averages
};

function fillLevels(root, levels, levelNum) {
    if (!root) return;

    if (levels.length === levelNum) {
        levels.push([ root.val ])
    } else {
        levels[levelNum].push(root.val)
    };

    fillLevels(root.left, levels, levelNum+1)
    fillLevels(root.right, levels, levelNum+1)
};

function average(array) {
    return array.reduce((a, b) => a +b) / array.length
};

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1

console.log(levelAverages(a)); // -> [ 3, 7.5, 1 ] 
