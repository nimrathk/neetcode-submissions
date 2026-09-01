class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea 1: put everything in a set
        # then loop through list & see if i+1+2+...n is in set
        # keep count of longest sequence

        # idea 2: sort the array and keep track of count
        # if you see a duplicate number just skip 

        if len(nums) == 0:
            return 0

        nSet = set(nums)
        max_seq = 1

        for n in nums:
            # check if n is the beginning of a sequence
            if n-1 in nSet:
                continue
            elif n+1 in nSet:
                count = 1
                num = n+1
                while num in nSet:
                    count += 1
                    num += 1
                if count > max_seq:
                    max_seq = count

        return max_seq