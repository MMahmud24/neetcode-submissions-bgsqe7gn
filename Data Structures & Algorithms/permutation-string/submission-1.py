class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        c = Counter(s1)
        while r-1 < len(s2):
            c2 = Counter(s2[l:r])
            if c2 == c:
                return True
            else:
                l += 1
                r += 1
        
        return False
