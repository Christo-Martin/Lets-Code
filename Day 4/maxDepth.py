class Solution:
    def maxDepth(self, s: str) -> int:
        n=0
        x=[]
        for i in s:
            if i =='(':
                n+=1
            elif i==')':
                x+=[n]
                n-=1
        if x:return max(x)
        return 0