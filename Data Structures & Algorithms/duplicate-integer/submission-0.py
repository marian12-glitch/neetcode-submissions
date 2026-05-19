class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            # check if num is in seen
            if num in seen:
                return True
            #if yes return True
            # add num to seen
            seen[num] = 1

        return False
