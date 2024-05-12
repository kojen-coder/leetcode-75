class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = 0
        result = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result