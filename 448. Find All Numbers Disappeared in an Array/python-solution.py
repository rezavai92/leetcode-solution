class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result =[0]*n
        
        for num in nums:
            result[num-1]=num
        
        print(result)
        i=0
        for f in range(n):
            if(result[f]==0):
                result[i]=f+1
                i+=1
        return result[:i]