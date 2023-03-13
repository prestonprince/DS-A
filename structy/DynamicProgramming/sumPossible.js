function sumPossible(amount, numbers, memo={}) {
    if (amount in memo) return memo[amount]
    if (amount < 0) return false;
    if (amount === 0) return true;

    for (const n of numbers) {
        if (sumPossible(amount-n, numbers) === true) {
            memo[amount] = true
            return memo[amount]
        }
    };

    memo[amount] = false;
    return memo[amount];
}

console.log(sumPossible(8, [5, 12, 4])); // -> true, 4 + 4
console.log(sumPossible(15, [6, 2, 10, 19])); // -> false
