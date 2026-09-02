class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        chars = {}
        l, r = 0, 1
        maxL = 1
        chars[s[l]] = 0

        while r < len(s):
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
                chars[s[r]] = r
            else:
                chars[s[r]] = r
            r += 1
            maxL = max(maxL, r-l)
        
        return maxL