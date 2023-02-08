// Write a function, compress, that takes in a string as an argument. 
// The function should return a compressed version of the string where consecutive 
// occurrences of the same characters are compressed into the number of occurrences followed by the character. 
// Single character occurrences should not be changed.

// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'

// You can assume that the input only contains alphabetic characters.

const compress = (s) => {
    // todo
    //set two pointers to 0
    // for the char
    let i = 0;
    // to find a different char
    let j = 0;
    
    let count = 0;
    let res = [];
    
    // iterate thru entire string + 1
    while (j < s.length + 1) {
        if (s[j] !== s[i]) {
        count = j - i;
        
        if (count === 1) {
            res.push(s[i])
        } else {
            res.push(`${count}${s[i]}`)
        }
        i = j
        }
        j++;
    };
    return res.join('')
}

console.log(compress('ccaaatsss')); // -> '2c3at3s'
