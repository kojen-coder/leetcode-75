class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif s == t:
            return True
        if len(s) == 0:
            return True
        else:
            index = 0
            for i in range(len(t)):
                if t[i] == s[index]:
                    index += 1
                if index == len(s):
                    return True
            return False