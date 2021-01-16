"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """similar to merge intervals, using heap approach. """
        ans = []
        OPEN, CLOSE = 0, 1
        events = []

        for emp in schedule:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()

        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))
            bal += 1 if cmd is OPEN else -1
            prev = t

        return ans
