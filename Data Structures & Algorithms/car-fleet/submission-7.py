class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        fleets = 0

        for i in range(len(position)):
            position[i] = (position[i], (target - position[i]) / speed[i])

        position.sort()

        curr_max = -1
        for i in range(len(position) - 1, -1, -1):
            if position[i][1] > curr_max:
                fleets += 1
                curr_max = position[i][1]

        return fleets

