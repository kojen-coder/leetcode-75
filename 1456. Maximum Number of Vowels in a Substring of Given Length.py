class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        answer = count

        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            if count > answer:
                answer = count
        return answer