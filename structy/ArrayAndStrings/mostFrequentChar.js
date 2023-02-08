// Write a function, mostFrequentChar, that takes in a string as an argument. 
// The function should return the most frequent character of the string. If there are ties, 
// return the character that appears earlier in the string.

// You can assume that the input string is non-empty.

const mostFrequentChar = (s) => {
    // todo
    let count = 0;
    let mostFrequent = '';
    let hashMap = {};
    
    // make char count hashmap
    for (const char of s) {
        hashMap[char] ? hashMap[char]++ : hashMap[char] = 1
    };
    
    // iterate over string again to maintain order and for each char,
    // check value for that char in hashmap
    // if value is greater than count, set count to that value and 
    // mostFrequent to that char
    for (const char of s) {
        if (hashMap[char] > count) {
        count = hashMap[char];
        mostFrequent = char
        }
    };
    
    return mostFrequent;
}

console.log(mostFrequentChar('bookeeper')); // -> 'e'
