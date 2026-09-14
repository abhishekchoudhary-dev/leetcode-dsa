# Problem: Leetcode 859 - Buddy strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/buddy-strings/description/
# Time Complexity: O(n) as we iterate over string
# Space Complexity: O(n) as we make hashmap
# Approach: Instead of keeping track of manually the previous mismatch and then checking if current mismatch can even be effectivety swapped with it we just keep a hashmap of values
# and then we just check that if the mismatches are 1 or >2 then any swap will disturb the string as we necessarily have to do one operation of swap and then its always false.
# so we only have to handle case of 0 mismatches and 2 mismatches which can swap with each other. For 0 mismatches we check if there is a key which has a value >1 and both hashmaps are equal 
# as this means we can just swap between same characters in both and then we return True else False.
# for exactly 2 mismataches which allow us 1 swap, we exactly check if both hashmaps are equal as if they are then swapping the 2 mismatches in on operation will
# match the strings with each other.

from collections import defaultdict
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        mismatch = 0
        even_key = False
        d = defaultdict(int)
        t = defaultdict(int)
        for i in range(len(s)):
            if s[i]!=goal[i]:
                mismatch+=1
            d[s[i]]+=1
            if d[s[i]] > 1 and not even_key:
                even_key = True
            t[goal[i]]+=1
        if mismatch==0:
            if d==t and even_key:
                return True
            else:
                return False
        elif mismatch==2 and d == t:
            return True
        return False