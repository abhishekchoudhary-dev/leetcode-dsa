# Problem: Leetcode 3450 - Maximum students on a single bench
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-students-on-a-single-bench/description/
# Time Complexity: O(n) we we go through the hashmap of the string
# Space Complexity: O(n) as we use hashmap which has keys equal to benches
# Approach: We add each bench in hashmap and add the benches as keys and each key has a set and then 
# we can have only unique students sitting on it. then we return the max len key. We can do so with generator expression also.

from collections import defaultdict
from typing import List
class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        d = defaultdict(set)
        for student,bench in students:
            d[bench].add(student)
        mx = 0
        for key,val in d.items():
            mx = max(mx,len(val))
        return mx
        #return max(len(v) for v in d.values())
    
        