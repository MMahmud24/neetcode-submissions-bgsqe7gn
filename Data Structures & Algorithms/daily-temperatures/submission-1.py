class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        count = 1
        for i in range(len(temperatures)):
            if (i == len(temperatures) - 1):
                result.append(0)
                break

            for j in range(i+1, len(temperatures)):
                if temperatures[i] >= temperatures[j]:
                    count += 1
                    if((j == len(temperatures) - 1)):
                        count = 0
                        break
                else:
                    break
            
            result.append(count)
            count = 1

        return result