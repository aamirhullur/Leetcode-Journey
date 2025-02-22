/**
 * @param {string} val
 * @return {Object}
 */

var expect = function(val){
    return {
        toBe: function(val2){
            if (val2 === val){
                return true;
            }else throw new Error("Not Equal")
        },
        notToBe: function(val2){
            if (val2 !== val){
                return true;
            }
            else throw new Error("Equal")
        }
    }
};