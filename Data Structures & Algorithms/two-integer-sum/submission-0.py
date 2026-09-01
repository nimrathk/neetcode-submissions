class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            if target - nums[i] in sums:
                ans = [sums[target-nums[i]], i]
                return ans
            sums[nums[i]] = i