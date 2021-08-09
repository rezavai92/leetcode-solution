/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMaxConsecutiveOnes = function(nums) {
    
    let i = nums.length-1
    
    let count =0
    let maximum_count =0
    while(i>=0){
        
        if(nums[i] & 1){
         count+=1   
        }
        else{
            count=0
        }
        
        maximum_count = Math.max(maximum_count,count)
        i--;
    }
    return maximum_count
    
};