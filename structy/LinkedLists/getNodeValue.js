class Node {
    constructor(val) {
        this.val = val;
        this.next = null
    }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

function getNodeValue(head, index) {
    let current = head;
    let idx = 0;
    
    while (current !== null) {
        if (idx === index) return current.val
        current = current.next
        idx += 1
    }
    return null
}

console.log(getNodeValue(a, 2)); // 'c')
