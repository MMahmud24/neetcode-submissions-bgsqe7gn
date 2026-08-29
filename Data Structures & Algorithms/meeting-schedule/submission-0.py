"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        heap = []

        for interval in intervals:
            heapq.heappush(heap, (interval.start, interval.end))

        end = -1 
        while heap:
            popped = heapq.heappop(heap)
            if popped[0] < end:
                return False

            end = popped[1]

        return True