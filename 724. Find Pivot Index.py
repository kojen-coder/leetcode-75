class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumR = sum(nums)
        sumL = 0
        for i, x in enumerate(nums):
            if sumL == (sumR - x - sumL):
                return i
            sumL += x
        return -1