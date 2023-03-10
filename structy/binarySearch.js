function binarySearch(arr, x, start, end) {
    if (start > end) return false;

    // find middle idx
    let mid = Math.floor((start + end)/2)

    if (arr[mid] === x) return true;

    if (arr[mid] > x) {
        return binarySearch(arr, x, start, mid-1)
    } else {
        return binarySearch(arr, x, mid+1, end)
    }
}

let arr = [1, 3, 5, 7, 8, 9];
let x = 5;

console.log(binarySearch(arr, x, 0, arr.length-1))
