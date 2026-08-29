"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        num_starts = 0
        s_p = 0
        e_p = 0
        max_rooms = 0
        while s_p < len(starts) and e_p < len(starts):
            if starts[s_p] < ends[e_p]:
                s_p += 1
                num_starts += 1
            else:
                num_starts -= 1
                e_p += 1
            
            max_rooms = max(num_starts, max_rooms)

        return max_rooms



