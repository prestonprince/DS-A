function minChange(amount, coins) {
    const res = _minChange(amount, coins);
    return res === Infinity ? -1 : res
}

function _minChange(amount, coins, memo={}) {
    if (amount in memo) return memo[amount];
    if (amount === 0) return 0;
    if (amount < 0) return Infinity;

    let smallest = Infinity;
    for (const coin of coins) {
        const possibleSmallest = 1 + _minChange(amount-coin, coins, memo);
        smallest = Math.min(possibleSmallest, smallest);
    };

    return memo[amount] = smallest
}
console.log(minChange(13, [1, 9, 5, 14, 30])); // -> 5
console.log(minChange(23, [2, 5, 7])); // -> 4
console.log(minChange(2017, [4, 2, 10])); // -> -1
