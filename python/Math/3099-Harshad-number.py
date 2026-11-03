# Problem: Leetcode 3099 - Harshad Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/harshad-number/description/
# Time Complexity: O(k) where k is the number of digits of the number
# Space Complexity: O(1)
# Approach - We simply find digit sum and then check if its divides or not


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(int(d) for d in str(x))
        if x%s==0:
            return s
        return -1
        