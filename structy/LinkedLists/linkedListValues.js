// Write a function, linkedListValues, that takes in the head of a linked list as an argument. 
// The function should return an array containing all values of the nodes in the linked list.

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
};

const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');

a.next = b;
b.next = c;
c.next = d;

const linkedListValues = (head) => {
    if (head === null) return []
    return [head.val].concat(linkedListValues(head.next))
};

console.log(linkedListValues(a)); // -> [ 'a', 'b', 'c', 'd' ]
