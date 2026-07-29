from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()      # Sort by start time

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                # Overlap: remove one interval.
                removals += 1
                # Keep the interval that ends earlier.
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removals