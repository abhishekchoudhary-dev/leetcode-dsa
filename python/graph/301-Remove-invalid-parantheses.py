# Problem: Leetcode 301 - Remove invalid parantheses
# Difficulty: Hard
# Link: https://leetcode.com/problems/remove-invalid-parantheses/description/
# Time Complexity: O(2^n) - as we explore all possible removals in DFS
# Space Complexity: O(n) as we keep a valid set to collect options
# Approach: First using left and right pointers we find the total amount of opening and closing brackets that are to be removed
# then we call our dfs function with empty string and the starting index and we always construct a string which has balance left and right ones and it removes all the unwanted brackets
# which is seen in our base case that only when both left_to_remove and right_to_remove go to zero only in that case do we append to the valid string.
# otherwise if our dfs find open brackets and there are left ones to remove we call our dfs again with left_to_remove -1
# same if closing is found and we have right_to_remove then we call it with right_to_remove - 1 and rest all the same ones.
# and we have a third general case which even if any of the first two run, we call by finding the 
# new_left and new_right count which account for the current character which will increment the right and left counts.
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def dfs(index, left_to_remove, right_to_remove, left_count, right_count, current_string):
            if index == string_length:
                if left_to_remove==0 and right_to_remove==0:
                    valid.add(current_string)
                return 
            #pruning if invalid for sure
            if string_length - index < left_to_remove + right_to_remove or left_count < right_count:
                return
            if s[index]=='(' and left_to_remove > 0:
                dfs(index+1, left_to_remove-1, right_to_remove, left_count, right_count, current_string)
            elif s[index]==')' and right_to_remove > 0:
                dfs(index+1, left_to_remove, right_to_remove-1, left_count,right_count, current_string)
            
            new_left_count = left_count+(1 if s[index]=='(' else 0)
            new_right_count = right_count+(1 if s[index]==')' else 0)
            dfs(index+1,left_to_remove,right_to_remove,new_left_count,new_right_count,current_string + s[index])
        left_to_remove = 0
        right_to_remove = 0
        for char in s:
            if char=='(':
                left_to_remove+=1
            elif char==')':
                if left_to_remove>0:
                    left_to_remove-=1
                else:
                    right_to_remove+=1
        valid = set()
        string_length = len(s)
        dfs(0,left_to_remove,right_to_remove,0,0,'')
        return list(valid)