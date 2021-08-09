/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
    
    let i=0
    let j = nums.length-1
    let result =[]
    
    for (let k=0;k<nums.length;k++){
        result[k] = 0
    }
    
    let k = result.length-1;
    
    while(i <=j){
        
        let num1 = Math.abs(nums[i])
        let num2 = Math.abs(nums[j])
        
        if(num1 > num2){
            result[k] = num1 * num1;
            i++;
        }
        else{
            result [k] = num2*num2;
            j--;
        }
        k--;
        
    }
    
    return result
    
};