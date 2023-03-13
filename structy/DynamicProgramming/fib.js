function fib(n, memo={}) {
    if (n in memo) return memo[n];

    if (n === 0 || n === 1) return n;

    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n]
};
console.log(fib(35)); // -> 9227465
