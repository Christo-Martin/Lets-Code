class Solution:
    def isThree(self, n: int) -> bool:
        s=0
        for i in range(2,n//2+1):
            if s==2:break
            if not n%i:
                s+=1
            
        return s==1
