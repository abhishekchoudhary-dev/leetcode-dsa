# Problem: Leetcode 4049 - Count values with equally spaced occurences I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-values-with-equally-space-occurrences-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we two hashmaps and a separate one to keep check on distances to avoid nested loops as that wont work
# Approach: We just make hashmap of frequencies and then we iterate over the values and see if it occurs thrice by checking length of its value list.
# while collecting the values we also use a hashmap of set to keep adding the distance between current index found and the previous index.
# the set will remove duplicated so that when we finally check if element occurs over 3 times, then if the len of that element value in the t hashmap is 1 that
# means only one distance was found between all indices which means they are equidistant and then we can increment our count variable.
# we return count at the end.

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