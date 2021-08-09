/**
 * @param {number[]} nums
 * @return {number}
 */

 var helper = function (num){
    let count =0
    while(num >0){
        
        count ++;
        num = parseInt(num/10)
    }
    return count
}
var findNumbers = function(nums) {
    
    let total =0
    for (let num of nums ){
        total += helper(num)%2==0?1:0
    }
    return total
    
};