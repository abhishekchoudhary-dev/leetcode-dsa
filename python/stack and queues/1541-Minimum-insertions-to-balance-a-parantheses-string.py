# Problem: Leetcode 1541 - Minimum insertion to balance a parantheses string
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-insertions-to-balance-a-parantheses-string/description/
# Time Complexity: O(n) as we go through the string
# Space Complexity: O(1) as we only use pointers
# Approach: We basically need to have realization then when an opening bracket is found and if there is any closing bracket before it
# then that closing bracket must be balanced first as balancing cannot be done across brackets. So when we find open bracket
# before incrementing the count of open we check for any close brackets present and balance it by adding to insertion if no open bracket is present
# and since balance is complete we set close_count is set 0. and if close brakcet found then if close count is 2
# then rest it to zero and if there is no open count then we add an open bracket else we just decrement open count by 1 else
# that particular open bracket has been balanced with the two close brackets that we just found
# once the loop ends we check the remaining open and close counts to see how many we need to insert to balance the leftover ones

class Solution:
    def minInsertions(self, s: str) -> int:

        '''
        #stack implementation
        stack = []
        insert = 0
        i = 0
        while i < len(s):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if i < len(s)-1 and s[i+1]==')':
                    i+=1
                else:
                    insert+=1
                if stack:
                    stack.pop()
                else:
                    insert+=1
            i+=1
        return insert + len(stack)*2 #as only open ones in stack
        '''
    
        close_count = open_count = 0
        insertion = 0
        for bracket in s:
            if bracket=='(':
                if close_count:#means previous imbalance left
                    if not open_count:
                        insertion+=2
                    else:
                        insertion+=(2-close_count)
                        open_count-=1
                    close_count=0
                open_count+=1
            else:
                close_count+=1
                if close_count==2:
                    close_count = 0
                    if not open_count:
                        insertion+=1
                    else:
                        open_count-=1
        if open_count == 0 and close_count==0:
            return insertion
        if open_count:
            insertion+=((open_count*2) - close_count)
            return insertion
        if close_count:
            insertion += close_count//2 + (close_count - (close_count//2)*2)*2
            return insertion