# This is solved in O(n)
# The easies approach is to sort this list first in descending order, then make a set of it to remove duplicates ,and then findout the third number. obviously you have to check if the length of the set is greater than equal to 3 or not. if not,then simply return the maximum value
# but sorting + removing duplicates will take O(nlogn)
# That's why this is solved in O(n) here
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n= len(nums)
        
        if(n < 3):
            
            return max(nums)
        
        else :
            
            f = nums[0]
            s=None
            t=None
            num = nums[1:]
            for c in num:
                if (c>f):
                    tmp=f
                    f=c
                    tmp1= s
                    s=tmp
                    t=tmp1
                    
                elif (c<f and s is not None and c > s):
                    
                    tmp = s
                    s = c
                    t = tmp
                elif (c<f and s is None):
                    s= c
                elif ( s is not None and c<s and t is None ):
                    t=c
                elif ( s is not None and t is not None and c<s and c>t):
                    t=c
                    
                print(f,s,t)
        if (t is None):
            return max(nums)
        else:
            return t
                    
                    