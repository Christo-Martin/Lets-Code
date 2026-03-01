class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        k=1
        for i in range(len(nums)):
            arr+=[nums[i+k]]
            k*=-1
        return arr
        