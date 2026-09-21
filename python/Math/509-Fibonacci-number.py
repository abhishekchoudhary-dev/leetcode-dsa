# Problem: Leetcode 509 - Fibonacci Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/fibonacci-number/description/
# Time Complexity: O(n)
# Space Complexity: O(n) for bottom up tabulation and O(1) for recursion
# Approach: We show both appraoch of bottom up tabulation which uses more space vs recursive approach which is basically top down dp

class Solution:
    def fib(self, n: int) -> int:
        #bottom up tabulation
        fibo = [0,1]
        for i in range(2,n+1):
            fibo.append(fibo[i-1]+fibo[i-2])
        return fibo[n]

        '''Recursive dp top down solutions
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        '''