class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # questions: 
        # are the arrays in ascending order?
        # what do i return if the list is empty?
        # can the list contain negative numbers?
        # can i use the .sort() method?

        # strat: use a prev variable that stores the previous value
        # check if the prev val == curr val via a for-each loop

        nums.sort()
        prev_val = float('-inf')

        for num in nums:
            if num == prev_val:
                return True
            prev_val = num
        
        return False

