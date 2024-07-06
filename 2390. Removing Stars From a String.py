class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        for i in s:
            if i == "*":
                if result:
                    result.pop()
            else:
                result.append(i)
        result = "".join(result) # concatenate all the strings in the list
        return result