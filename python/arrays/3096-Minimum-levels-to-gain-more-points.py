
# Problem: Leetcode 3096- Minimum levels to gain more points
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we keep prefix sum
# Approach: Simple prefix sum problem where we take the prefix sum and then we loop over it
# and then we see if at any point prefix sum crosses the sum of the remaining possible array
# and we immediately return the index. if loop ends we return -1

from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        prefix = [0]*(len(possible)+1)
        score = 0
        for i in range(len(possible)):
            if possible[i]==1:
                score+=1
            else:
                score-=1
            prefix[i+1] = score
        for i in range(1,len(prefix)-1): 
            #iterate upto -1 as bob needs to play one level
            if prefix[i-0] > prefix[-1] - prefix[i]:
                return i
        return -1