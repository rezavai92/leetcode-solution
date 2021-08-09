class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i =len(nums)-1
        c=0
        m=0
        while(i>=0):
            if(nums[i] & 1 ):
                c+= 1
            
            else:
                c=0
            
            m = max(m,c)
            
            i-=1
        return m
        
        
        