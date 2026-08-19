class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mappings = [0] * len(position)
        for i in range(len(position)):
            mappings[i] = [position[i], speed[i]]

        mappings.sort()

        fleets = 0

        time_to_finish = [0] * len(mappings)

        for i in range(len(mappings)):
            time_to_finish[i] = (target - mappings[i][0]) / mappings[i][1]

        curr_max = -1
        for i in range(len(mappings) - 1, -1, -1):
            if time_to_finish[i] > curr_max:
                fleets += 1
                curr_max = time_to_finish[i]

        return fleets

