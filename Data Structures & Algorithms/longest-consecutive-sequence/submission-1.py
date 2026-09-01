class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea 1: put everything in a set
        # then loop through list & see if i+1+2+...n is in set
        # keep count of longest sequence

        # idea 2: sort the array and keep track of count
        # if you see a duplicate number just skip 

        if len(nums) == 0:
            return 0

        nums.sort()
        count, max_seq = 1, 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] + 1 == nums[i]:
                count += 1
                if count > max_seq:
                    max_seq = count
            else:
                count = 1

        return max_seq