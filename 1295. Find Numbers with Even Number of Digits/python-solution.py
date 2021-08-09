class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def helper (num):
            count =0
            while(num>0):
                count+=1
                num=int(num/10)
            return count
        
        evenTotal =0
        for num in nums:
            if(helper(num)%2==0 ):
                evenTotal +=1
        return evenTotal