class Solution:
    def averageValue(self, nums: List[int]) -> int:
        m=0
        n=0
        for i in nums:
            if not i%6:
                n+=i
                m+=1
        if m:return n//m
        return 0