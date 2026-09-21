# Problem: Leetcode 507 - Perfect number
# Difficulty: Easy
# Link: https://leetcode.com/problems/perfect-number/description/
# Time Complexity: O(sqrt(num))
# Space Complexity: O(1) 
# Approach: We technically need to loop till num//2 and find all sum of divisors but that does not work due to time complexity 
# as the size is 10^8. So we loop till sqrt of number using the fact that any factors of the number has a mirror factor on the other side of the sqrt.
# so when we find a factor we add it and its mirror directly to the total and at the end we add 1
# as we are starting from 1. Then at end we check if total == num


import math;
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        
        def divisors(num)->list[int]:
            total = 0
            for i in range(2,math.isqrt(num)+1):
                if num%i==0:
                    total+=i
                    total+=num//i
                    #factors come in pairs
            return total+1

        return divisors(num) == num