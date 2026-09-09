class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            else:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    if l != mid:
                        l = mid
                    else:
                        return nums[r]
        
        return nums[mid]