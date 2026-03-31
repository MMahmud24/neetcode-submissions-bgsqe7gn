class MinStack:

    def __init__(self):
        self.topNum = 0
        self.stk = []
        self.allMins = [float('inf')]
        self.minTop = 1

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.topNum += 1
        if val <= self.allMins[self.minTop - 1]:
            self.min = val
            self.allMins.append(val)
            self.minTop += 1

    def pop(self) -> None:
        if self.top() == self.allMins[self.minTop - 1]:
            self.minTop -= 1
            self.allMins = self.allMins[:self.minTop]
        self.topNum -= 1
        self.stk = self.stk[0:self.topNum]

    def top(self) -> int:
        return self.stk[self.topNum - 1]
    

    def getMin(self) -> int:
        return self.allMins[self.minTop - 1]
