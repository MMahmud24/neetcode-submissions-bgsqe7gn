class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result = result + str + "π"

        return result
    def decode(self, s: str) -> List[str]:
        strs = []
        curr = ""
        for x in s:
            if x != "π":
                curr = curr + x
            else:
                strs.append(curr)
                curr = ""
        
        return strs 