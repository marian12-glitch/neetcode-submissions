class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #track maxCount
        #use a set, cast the list into a set
        #the first number does not have  andother number 1 below
        #use a while loop to find n+1 ... n+n

        maxCount = 0

        num_set = set(nums)


        for n in num_set:
            if (n-1 not in num_set):
                l = 1

                while (n + l in num_set):
                    l +=1

                    
                maxCount = max( l, maxCount)

        return maxCount


               

