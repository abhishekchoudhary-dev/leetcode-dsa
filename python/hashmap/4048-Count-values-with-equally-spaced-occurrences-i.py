# Problem: Leetcode 4048 - Count values with equally spaced occurences I
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-values-with-equally-space-occurrences-i
# .py/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We just make hashmap of frequencies and then we iterate over the values and see if it occurs thrice by checking length of its value list and 
# if it does then we check distance between the three and if its equal we increment count and return cnt at the end

from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cnt = 0
        d = defaultdict(list)
        for i, num in enumerate(nums):
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]
        for k,v in d.items():
            if len(v)==3:
                if v[1]-v[0] == v[2]-v[1]:
                    cnt+=1
        return cnt