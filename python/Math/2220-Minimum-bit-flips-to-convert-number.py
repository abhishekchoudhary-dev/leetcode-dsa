# Problem: Leetcode 2220 - Minimum bit flips to convert number
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
# Time Complexity: O(k) where k is the max number of bits between start and goal
# Space Complexity: O(1)
# Approach - We just xor both which will find the different bits and then calculate the number of different bits
# We can also convert both to string the binary representations of the two numbers
# Approach2 - We use brian kerningham algorithm, where we keep doing & with number and number - 1 which will keep setting the LSB 1 to 0
# and end up with 0000000 all zeros. so the number of 1 bits(which were diff after xor) need to be set to 0
# so we can keep doing this in a loop and increment count before the xor goes to zero.


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start^goal
        return xor.bit_count()
        '''
        if start > goal:
            start,goal = goal,start
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        start = '0'* (len(goal) - len(start)) + start
        return sum(1 for i in range(len(start)) if start[i]!=goal[i])
        '''