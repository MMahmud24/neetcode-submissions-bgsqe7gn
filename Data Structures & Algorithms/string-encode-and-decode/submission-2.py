class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result

        return result
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        j = i
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            l = int(s[i:j])
            i = j + 1
            j = j + l + 1

            strs.append(s[i:j])

            i = j

        return strs