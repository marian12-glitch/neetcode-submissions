class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount =  0
        num_set = set(nums)

        for n in nums:
            
            if (n - 1) not in num_set:
                l = 1

                while (n + l) in num_set:
                    l += 1

                maxCount = max(l, maxCount)

        return maxCount
              

               

