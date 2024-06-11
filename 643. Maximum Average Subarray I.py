class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best_total = now = sum ( nums[0:k] )

        for i in range ( k, len ( nums ) ):
            now += nums[i] - nums[i - k]
            if now > best_total:
                best_total = now
        return best_total / k