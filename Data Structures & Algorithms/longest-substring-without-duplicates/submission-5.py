class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] in s[l:r] and r != l:
                res = max(res, r-l)
                l += 1
            else:
                r += 1

        res = max(res, r-l)
        return res
        
