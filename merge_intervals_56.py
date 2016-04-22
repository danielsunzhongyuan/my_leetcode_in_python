# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
            result = self.insert(result, interval)
        return result

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        length = len(intervals)

        leftPosition = self.findPosition(intervals, newInterval.start)
        rightPosition = self.findPosition(intervals, newInterval.end)
        if rightPosition == 0 and newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        elif newInterval.start <= intervals[leftPosition].end:
            e = max(intervals[rightPosition].end, newInterval.end)
            s = min(intervals[leftPosition].start, newInterval.start)
            return intervals[0:leftPosition] + [Interval(s, e)] + intervals[rightPosition+1:]
        else:
            e = max(intervals[rightPosition].end, newInterval.end)
            return intervals[0:leftPosition+1] + [Interval(newInterval.start, e)] + intervals[rightPosition+1:]

    def findPosition(self, intervals, number):
        start, end = 0, len(intervals) - 1
        while start < end:
            mid = (start + end) / 2
            if intervals[mid].start <= number <= intervals[mid].end:
                return mid
            elif number < intervals[mid].start:
                end = mid - 1
            else:
                start = mid + 1
        if start == 0 or end == 0:
            return 0
        if number < intervals[end].start:
            return end - 1
        else:
            return end
