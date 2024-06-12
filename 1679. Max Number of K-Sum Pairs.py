class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort ()
        left, right, count = 0, len ( nums ) - 1, 0

        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                left += 1
                right -= 1
                count += 1
        return count