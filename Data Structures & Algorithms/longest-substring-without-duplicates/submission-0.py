class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize pointer L and R
        L, R = 0, 0
        # initialize set
        seen = set()
        #initialize counter
        maxSeq = 0
        currCount = 0

        while R < len(s):
            if not(s[R] in seen):
                seen.add(s[R])
                currCount += 1
                maxSeq = max(maxSeq, currCount)
                R +=1

            else:
                seen.remove(s[L])
                L +=1
                currCount = R - L

        return maxSeq
