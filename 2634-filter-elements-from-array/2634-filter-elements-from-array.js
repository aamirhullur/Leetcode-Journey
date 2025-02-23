/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// var filter = function(arr, fn) {
//     var filteredArr = [];
//     for (var i = 0; i < arr.length; i++) {
//         if (fn(arr[i], i)) {
//             filteredArr.push(arr[i]);
//         }
//     }
//     return filteredArr;
// };

var filter = function(arr, fn) {
    let res = [];
    for (const i in arr){
        if (fn(arr[i], Number(i))){
            res.push(arr[i])
        }
    }
    return res;
};