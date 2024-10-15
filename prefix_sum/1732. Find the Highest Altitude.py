class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        value = 0
        max_value = 0
        for i in range(len(gain)):
            value += gain[i]
            if value > max_value:
                max_value = value
        return max_value