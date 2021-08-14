class Solution:
    
   
        
    def getRow(self, rowIndex: int) -> List[int]:
        
        arr=[[1],[1,1]]
        
        if rowIndex==0:
            return arr[0]
        elif rowIndex ==1:
            return arr[1]
        
        else:
           
            for i in range(2,rowIndex+1):
                li=[]
            
                for j in range(i+1):
                    if(j==0 or j==i):
                        li.append(1)
                    else:
                        li.append(arr[i-1][j-1]+ arr[i-1][j] )
                arr.append(li)
                
        return arr[rowIndex]
                    