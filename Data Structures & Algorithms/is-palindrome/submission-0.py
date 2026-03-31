class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first = 0
        last = len(s) - 1

        while first < last:
            while first < last and not self.checkChar(s[first]):
                first +=1
            while first < last and not self.checkChar(s[last]):
                last -= 1
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1
        
        return True

    def checkChar(self, c):
        return ((ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9')))