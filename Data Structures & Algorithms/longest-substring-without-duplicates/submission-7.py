class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        sett = set()
        while r < len(s):
            if s[r] in sett and r != l:
                res = max(res, r-l)
                sett.remove(s[l])
                l += 1
            else:
                sett.add(s[r])
                r += 1

        res = max(res, r-l)
        return res
        
