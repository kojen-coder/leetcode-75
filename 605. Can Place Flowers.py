class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, count = 0, 0
        for i in flowerbed:
            if i == 1:
                if prev == 1:
                    count -= 1
                prev = 1

            elif i == 0:
                if prev == 0:
                    count += 1
                    prev = 1
                else:
                    prev = 0
        return count >= n