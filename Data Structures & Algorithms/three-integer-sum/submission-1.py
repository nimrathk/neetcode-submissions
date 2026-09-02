class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # almost like binary search for each number--> go left if too high etc
        res = []

        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:  
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res
