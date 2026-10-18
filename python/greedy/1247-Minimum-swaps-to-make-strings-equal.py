# Problem: Leetcode 1247 - Minimum swaps to make strings equal
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only use pointers
# Approach: We count the xy and yx type mismatches. then each same type mismatch takes one move to solve
# so xy count + 1 // 2 and same for yx type of mismtaches. if mismatches are oppositive then they take two moves
# which is recorded in our formula. if total mismatches are odd then there is no solution.
# this is greedy because optimal strategy at each stage finds the correct global result.
# Hence i just take the optimat strategy by keeping a counter and then take the pairs like how 
# many i have to get the answer

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
       
        i = 0
        xy_type=yx_type = 0
        while i< len(s1):
            if s1[i]!=s2[i]:
                if s1[i]=='x' and s2[i]=='y':
                    xy_type+=1
                else:
                    yx_type+=1
            i+=1
        
        if (xy_type+yx_type)%2==1:
            return -1
        return (xy_type+1)//2 + (yx_type+1)//2