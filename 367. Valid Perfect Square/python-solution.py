class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num ==0 or num ==1):
            return True
        def binary_search(left,right,num):
            
            if(left>right ):
                return False
            mid = (left + right)//2
            
            if(mid*mid==num):
                return True
            elif (mid*mid > num):
                return binary_search(left,mid-1,num)
            else:
                return binary_search(mid+1,right,num)
            return False 
        return binary_search(0,num,num)
        