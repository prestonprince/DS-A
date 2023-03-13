function pairedParentheses(str) {
    let count = 0;

    for (const char of str) {
        if (char === '(') count+=1;
        if (char === ')') {
            if (count === 0) return false;
            count-=1
        }
    };

    if (count !== 0) return false;
    return true
}

console.log(pairedParentheses("(((potato())))")); // -> true
