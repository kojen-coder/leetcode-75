class Solution:
    def decodeString(self, s: str) -> str:
        def helper(x, s):
            n = len(s)
            ans, multiplier = '', 0
            while x < n:
                char = s[x]
                if char.isdigit():
                    multiplier = multiplier*10 + int(char)
                elif char == '[':
                    encoded, x = helper(x + 1, s)
                    ans += multiplier * encoded
                    multiplier = 0
                elif char == ']':
                    return ans, x
                else:
                    ans += char
                x += 1
            return ans, n
        return helper(0, s)[0]
