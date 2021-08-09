class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i =0
        j = len(nums)-1
        r=[0 for f in range(j+1)]
        k=j
        while(i<=j):
            num1 = abs(nums[i])
            num2 = abs(nums[j])
            
            if(num1>num2):
                r[k]= num1*num1
                i+=1
                
            else:
                r[k] = num2*num2
                j-=1
            k-=1
            
        return r
        