# Problem: Leetcode 2748 - Number of beautiful pairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-beautiful-pairs/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just do a nested loop based on constraints and then we just check the gcd of the two numbers
# that is the first digit of first number and second of another to be 1. if yes then we increment our pair count

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt = 0
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        for i in range(len(nums)-1):
            fd = int(str(nums[i])[0])
            for j in range(i+1,len(nums)):
                sd = int(str(nums[j])[-1])
                if gcd(fd,sd)==1:
                    cnt+=1
        return cnt