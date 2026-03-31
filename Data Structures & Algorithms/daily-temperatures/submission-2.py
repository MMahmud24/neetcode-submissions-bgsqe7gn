class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                popped = stk.pop()
                index = popped[1]
                diff = i - index
                res[index] = diff 

            stk.append((temperatures[i], i))


        return res