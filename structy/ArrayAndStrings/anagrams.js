/* 
Write a function, anagrams, that takes in two strings as arguments. 
The function should return a boolean indicating whether or not the strings are anagrams. 
Anagrams are strings that contain the same characters, but in any order.
*/

const anagrams = (s1, s2) => {
    // todo
    // make sure both strings are same length
    if (s1.length !== s2.length) return false
    
    // instantiate two hashmaps, one for each string
    const hashMap1 = {};
    const hashMap2 = {};
    
    // we will populate the hashmaps with keys being each char, and the value being 
    // how many times the char appears in the string
    for (const char of s1) {
      hashMap1[char] ? hashMap1[char]++ : hashMap1[char] = 1
    };
    
    for (const char of s2) {
      hashMap2[char] ? hashMap2[char]++ : hashMap2[char] = 1
    };
    
    // iterate thru key and value of first hashmap
    for (const [key, value] of Object.entries(hashMap1)) {
      // check second hashmap to see if it has the key, if it does
      // check if its value at that key matches the first hashmaps value at that key
      // if either is false, return false
      if (!hashMap2[key] || hashMap2[key] !== value) {
        return false
      }
    };
    
    return true
  };

console.log(anagrams('restful', 'fluster')); // -> true
