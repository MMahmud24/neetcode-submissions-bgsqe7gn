class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = {"+": 1, "-": 2, "*":3, "/":4}

        stk = []

        for x in tokens:
            if x not in d:
                stk.append(int(x))
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                if d[x] == 1:
                    stk.append(num1 + num2)
                if d[x] == 2:
                    stk.append(num1 - num2)
                if d[x] == 3:
                    stk.append(num1 * num2)
                if d[x] == 4:
                    div = num1 / num2
                    if div < 0:
                        div = math.ceil(div)
                    else:
                        div = math.floor(div)
                    
                    stk.append(div)

        return stk[0]