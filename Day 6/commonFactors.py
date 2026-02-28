class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        k=1
        for i in range(2,min(a,b)+1):
            if not(a%i or b%i):
                k+=1
        return k
        