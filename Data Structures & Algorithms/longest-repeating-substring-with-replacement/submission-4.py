class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find maxvalid window r
        maxWindowSize = 0
        maxFreq = 0
        seen = {}
        L, R = 0, 0

        while R < len(s):
            seen[s[R]] = seen.get(s[R], 0) + 1
            maxFreq = max(maxFreq, seen[s[R]])

            if (R - L + 1) - maxFreq > k:
                seen[s[L]] -= 1
                L += 1

            maxWindowSize = max(maxWindowSize, R - L + 1)
            R += 1

        return maxWindowSize
            