# Problem: Leetcode 4057 - Number of intersecting interval pairs II
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1) 
# Approach: We sort intervals with start values. then we record the starts in another array and doing this as 
# second step ensures that starts are already sorted so that binary search will work directly. 
# Then for each interval we do the binary search for start in starts array and update count. This is done in O(1) time
# as idx - 1 - (current_interval_idx) will give us how many intervals the current interval overlaps with.

from bisect import bisect_right
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        cnt = 0
        starts = [interval[0] for interval in intervals]
        for i in range(len(intervals)-1):
            curr_end = intervals[i][1]
            idx = bisect_right(starts,curr_end)
            cnt+= idx - 1 - i
        return cnt

        '''
        #brute force does not work here
        intervals.sort(key=lambda x:x[0])
        cnt = 0
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[j][0] > intervals[i][1]:
                    break
                cnt+=1
        return cnt
        '''
        