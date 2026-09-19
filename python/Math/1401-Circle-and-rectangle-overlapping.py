# Problem: Leetcode 1401 - Circle and rectangle overlapping
# Difficulty: Medium
# Link: https://leetcode.com/problems/circle-and-rectangle-overlapping/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: We first keep circle in middle and check for either rectangle is fully outside the cicle range 
# or otherwise we check each quadrant for overlap by checking if the radius can reach the closes vertex of the rectangle.


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter + radius < x1 or xCenter-radius >x2 or yCenter+radius < y1 or yCenter - radius > y2:
            return False
        val = radius*radius
        if x1>xCenter and y1>yCenter and val < (x1-xCenter)**2 + (y1-yCenter)**2:
            return False
        if x1 >xCenter and y2<yCenter and val < (x1-xCenter)**2 + (y2-yCenter)**2:
            return False
        if x2<xCenter and y2 < yCenter and val < (x2-xCenter)**2 + (y2-yCenter)**2:
            return False
        if x2<xCenter and y1>yCenter and val < (x2-xCenter)**2 + (y1-yCenter)**2:
            return False
        return True 