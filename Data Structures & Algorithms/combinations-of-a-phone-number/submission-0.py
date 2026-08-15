class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        res, sol = [], []
        mapping = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def backtrack():
            if len(sol) == len(digits):
                res.append("".join(sol[:]))
                return
            for letter in mapping[int(digits[len(sol)])-2]:
                sol.append(letter)
                backtrack()
                sol.pop()

        backtrack()
        return res
        