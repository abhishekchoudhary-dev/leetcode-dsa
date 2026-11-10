# Problem: Leetcode 4103 - Remove elements by type and color
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-elements-by-type-and-color/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a stack
# Approach: We make runs where we combines each group in their consecutive order and then to simulate dropping 
# we take a stack and keep adding elements and if element in middle drop we combine the other elements together and increase count accordingly.
#We find run in a for loop and then we iterate over the runs and keep a stack to recombine runs split across different groups. For each run total 
# value before or after combining we just need to check if groupSize[runtype] will divide its value and if it does then this run can be dropped eventually.
#  If none of the above is possible we append the element to the stack. At the end we check if len(stack)==0

from collections import defaultdict
class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        type_colors = list(zip(types,colors))
        runs = []
        for i in range(len(type_colors)):
            if runs and type_colors[i] == type_colors[i-1]:
                runs[-1][1]+=1
            else: 
                runs.append([type_colors[i],1])
      
        stack = []
        for element in runs:
            if element[1] % groupSize[element[0][0]]==0:
                continue
            if stack and stack[-1][0] == element[0]:
                stack[-1][1] += element[1]
                if stack and stack[-1][1] % groupSize[stack[-1][0][0]]==0:
                    stack.pop()
            else:
                stack.append(element)
        return len(stack)==0