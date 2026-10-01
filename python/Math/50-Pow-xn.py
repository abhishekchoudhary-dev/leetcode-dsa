# Problem: Leetcode 50 - Power(x,n)
# Difficulty: Medium
# Link: https://leetcode.com/problems/pow(x,n)/description/
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: We use binary exponentiation instead of usual exponentiation which keeps the calculation limited.
# besically the power is converted to binary number and we take only those powers of the base which have the bit set. 
# If the bit is set, we take that powers otherwise we dont and for each iteration the base is doubled.
# and we keep moving forward with it.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)
        #we dont increase the number directly beyond the range
        #base keeps doubling and we only take relevant powers

        #return pow(x,n) - Solution using in built function
        ans = 1
        if n==0: return 1
        if n<0:
            x = 1.0/x
            n = -1 * n
        while n!=0:
            if n%2==1:
                ans*=x
                n-=1
            x*=x #square the base
            n//=2
        return ans