class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        # fill the dict with s
        for char in s:
            if char in seen:
                seen[char] += 1

            else:
                seen[char] = 1
        
        # for each char in t check if it is in seen and reduce by 1
        for char in t:
            if char in seen:
                seen[char] -= 1

            else:
                return False

        #return for all values in seen == 0
        return all(val == 0 for val in seen.values())