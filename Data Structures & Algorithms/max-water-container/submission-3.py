class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_vol = 0

        while end > start:
            curr_vol = (end - start) * min(heights[start], heights[end])
            max_vol = max(max_vol, curr_vol)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_vol
