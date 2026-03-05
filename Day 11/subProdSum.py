class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n:
            a=n%10
            n//=10
            p*=a
            s+=a
        return p-s