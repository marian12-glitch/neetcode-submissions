class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # Initialize L and R pointers
       L,R = 0, 0
       # track Current Count and Max count
       currCount, maxCount = 0, 0

       seen = set()
       # window between L and R
       while R < len(s):
        # if pointer R is in set, remove L
            if not(s[R] in seen):
                seen.add(s[R])
                currCount +=1
                maxCount = max(currCount, maxCount)
                R +=1
            else:
                seen.remove(s[L])
                L +=1
                currCount = R - L
            #if not add R

       return maxCount
       