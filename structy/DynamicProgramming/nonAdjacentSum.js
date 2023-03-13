function nonAdjacentSum(nums, i=0, memo={}) {
    if (i in memo) return memo[i];
    if (i >= nums.length) return 0;

    const include  = nums[i] + nonAdjacentSum(nums, i+2, memo);
    const exclude  = nonAdjacentSum(nums, i+1, memo);

    memo[i] = Math.max(include, exclude);
    return memo[i]
}

const nums = [
    72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
    30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
    83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
    61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
    30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
    72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
    42
  ];
console.log(nonAdjacentSum(nums)); // -> 1465
