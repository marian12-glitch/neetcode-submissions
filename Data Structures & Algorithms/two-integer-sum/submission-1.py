class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        #run a for loop
        for i, num in enumerate(nums) :
            C = target - num
        #find the compliment target - num
        #if compliment in seen
            if C in seen:
            # return index of num and index of compliment
                return [ seen[C], i]
                
            #else store the value of compliment and its index in seen
            else:
                seen[num] = i