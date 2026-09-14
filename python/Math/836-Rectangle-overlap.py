# Problem: Leetcode 836 - Rectangle overlap
# Difficulty: Easy
# Link: https://leetcode.com/problems/rectangle-overlap/description/
# Time Complexity: O(1) as we check the overlap directly
# Space Complexity: O(1) as we dont use any extra space
# Approach: We place one rectangle on the left and right of the other rectangle and check if it matches the condition of having no overlap.
# If yes we inmmmediately return False. If all the boundary checks succeed then we straight return True

from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        #sides overlap
        #top right
        if x4<=x1 or x2<=x3:
            return False
        if y1>=y4 or y3>=y2:
            return False
        if x4>x1 and (y1>=y4 or y3>=y2):
            return False
        if x3<x2 and (y1>=y4 or y3>=y2):
            return False
        return True