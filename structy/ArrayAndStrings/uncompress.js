// Write a function, uncompress, that takes in a string as an argument. 
// The input string will be formatted into multiple groups according to the following pattern

{/* <number><char>

for example, '2c' or '3a'. */}

/* 
    3a2b1c
    23C3a4b
    Iterate through string
    Setup 2 pointers(1 for numbers, 1 for characters)
    First pointer at the beginning
    Second pointer iterating through until it finds a ascii character
        For loop for however many times the value of the first pointer is
            each loop push the value of the second pointer into the result string

*/

// The function should return an uncompressed version of the string where each 'char' 
// of a group is repeated 'number' times consecutively. You may assume that the input string is 
// well-formed according to the previously mentioned pattern.

const uncompress = (s) => {
    let i = 0;
    let j = 0;
    let mult = 0;
    let res = [];
    const nums = '0123456789'

    while (j < s.length) {
        if (nums.includes(s[j])) {
            j++
        } else {
            mult = s.slice(i, j)
            for (let k = 0; k < mult; k++) {
                res.push(s[j])
            }
            j++
            i = j
        }
    }
    return res.join('')
}

// Time complexity
// O(nm)

console.log(uncompress("100C3a1t")); // -> 'CCaaat'
