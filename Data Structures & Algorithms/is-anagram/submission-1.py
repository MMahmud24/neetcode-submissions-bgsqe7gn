from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for letter in s:
            d1[letter] += 1
        for letter in t:
            d2[letter] += 1
        
        return d1 == d2