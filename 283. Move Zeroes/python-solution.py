class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j= 0
        while(i < len(nums)):
            if(nums[i] ==0 ):
                i+=1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
                i+=1
                j+=1
        return nums