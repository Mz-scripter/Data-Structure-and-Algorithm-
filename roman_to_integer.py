class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        summ = 0
        i = 0
        n = len(s)

        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i + 1]]:
                summ += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        return summ


result = Solution()

print(result.romanToInt('MCMXCIV'))
