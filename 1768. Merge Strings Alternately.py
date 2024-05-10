class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        list = []
        for i in range(min(len(word1), len(word2))):
            list.append(word1[i])
            list.append(word2[i])
        return ''.join(list)