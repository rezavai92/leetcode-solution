class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=len(arr)-1
        current_max = 0
        while(i>=0):
            if(i==len(arr)-1):
                current_max=arr[i]
                arr[i] = -1
            else:
                tmp=arr[i]
                arr[i]= current_max
                current_max= max(current_max,tmp)
            i-=1
        return arr
        