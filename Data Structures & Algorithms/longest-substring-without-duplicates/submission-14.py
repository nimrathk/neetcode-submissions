from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 0
        chars = defaultdict(str)
        maxLen = 0

        while r < len(s) and l <= r:
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1 if chars[s[r]] + 1 > l else r+1
                chars[s[r]] = r
            else:
                chars[s[r]] = r
            # print("start: " + str(l))
            # print("r: " + str(r))
            # print(chars)
            maxLen = max(maxLen, r-l+1)
            # print("MaxLen: " + str(maxLen))
            r += 1

        return maxLen