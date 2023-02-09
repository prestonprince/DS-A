// Write a function, pairProduct, that takes in an array and a target product as arguments. 
// The function should return an array containing a pair of indices whose elements multiply to the given target. 
// The indices returned must be unique.

// Be sure to return the indices, not the elements themselves.

// There is guaranteed to be one such pair whose product is the target.

const pairProduct = (numbers, targetProduct) => {
    const hashMap = {};
    // here, we are going to populate the hashmap as we iterate over our numbers array
    for ( let i = 0; i < numbers.length; i++ ) {
      const n = numbers[i];
      
      // and at each element we will divide the target sum by the element
      const quotient = targetProduct / n
      
      // and then check if our hashmap contains this quotient
      if ( quotient in hashMap ) {
        // if it does, return current index and value of quotient in hashmap
        return [ i, hashMap[quotient] ]
      } else {
        // if not, add element as key to hashmap with its value being the element's corresponding index
        hashMap[n] = i
      }
    };
};

console.log( pairProduct([3, 2, 5, 4, 1], 10) ); // -> [1, 2]
