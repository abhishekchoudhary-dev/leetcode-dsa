
# Problem: Leetcode 1385 - Find distance value between two arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-distance-value-between-two-arrays/description/
# Time Complexity: O(n)
# Space Complexity: O(n) 
# Approach: We just run a nested loop based on constraints and check if an element has distance less than 
# d for values in arr2 and increment count

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt = 0
        for num1 in arr1:
            possible = True
            for num2 in arr2:
                if abs(num1-num2) <= d:
                    possible=False
                    break
            if possible:
                cnt+=1
        return cnt