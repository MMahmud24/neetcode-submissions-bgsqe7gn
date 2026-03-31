class Solution:
    def isValid(self, s: str) -> bool:
    
        d = {"(": ")", "{" : "}", "[" : "]"}
        
        stk = []
        for symbol in s:
            if symbol in d:
                stk.append(symbol)
            if symbol not in d:
                if (stk):
                    popped = stk.pop()
                    if symbol != d[popped]:
                        return False
                else:
                    return False
        
        if (stk):
            return False
        
        return True