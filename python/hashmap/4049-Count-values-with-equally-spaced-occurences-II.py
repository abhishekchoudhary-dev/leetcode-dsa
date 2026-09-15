# Problem: Leetcode 4049 - Count values with equally spaced occurences I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-values-with-equally-space-occurrences-i
# .py/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We just make hashmap of frequencies and then we iterate over the values and see if it occurs thrice by checking length of its value list and 
# if it does then we check distance

from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
    
        cnt = 0
        d = defaultdict(list)
        t = defaultdict(set)
        for i, num in enumerate(nums):
            if num in d:
                last = d[num][-1]
                d[num].append(i)
                t[num].add(i-last)
            else:
                d[num] = [i]
        #print(d,t)
        for num,indices in d.items():
            if len(indices)>=3:
                if len(t[num])==1:
                    cnt+=1
                
        return cnt