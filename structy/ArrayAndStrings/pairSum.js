// Write a function, pairSum, that takes in an array and a target sum as arguments. 
// The function should return an array containing a pair of indices whose elements sum to the given target. 
// The indices returned must be unique.

// Be sure to return the indices, not the elements themselves.

// There is guaranteed to be one such pair that sums to the target.

const pairSum = (numbers, targetSum) => {
    // todo
    const hashMap = {};
    
    // populate hashmap with keys being each number in numbers array, and values
    // being their corresponding index
    for (let i = 0; i < numbers.length; i++) {
      const n = numbers[i];
      // find difference between the target sum and the current num
      // this will be the number we want to look up in our hashmap
      const difference = targetSum - n;
      if (difference in hashMap) {
        return [i, hashMap[difference]]
      };
      hashMap[n] = i
    }
  };

console.log(pairSum([3, 2, 5, 4, 1], 8)); // -> [0, 2]
