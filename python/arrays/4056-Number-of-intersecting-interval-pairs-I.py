# Problem: Leetcode 4056 - Number of intersecting intervals pairs I
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-intersecting-interval-pairs-I/description
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Based on input size we can just run a nested loop to check the intervals overlapping. we first sort the the intervals and then check pairs
# if they are overlapping and increment count. Since intervals are sorted by x[0] we can even break early if the start of interval at j is already higher than the current 
# intervals upper bound


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        cnt = 0
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]>=intervals[j][0]:
                    cnt+=1
        return cnt