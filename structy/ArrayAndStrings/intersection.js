// Write a function, intersection, that takes in two arrays, a,b, as arguments. 
// The function should return a new array containing elements that are in both of the two arrays.

// You may assume that each input array does not contain duplicate elements.

const intersection = (a, b) => {

    const res = [];
    // populate a set (no duplicates) with first array 
    const mySet = new Set(a);
    
    // iterate thru second array, checking if each element is in the set
    // if so, push element to result array 
    for ( const n of b ) {
      if ( mySet.has(n) ) res.push(n)
    }
    
    return res;
};

console.log( intersection([4,2,1,6], [3,6,9,2,10]) ) // -> [2,6]
