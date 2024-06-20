class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        unique_value = []
        for i in count:
            if count[i] in unique_value:
                return False
            else:
                unique_value.append(count[i])
        return True