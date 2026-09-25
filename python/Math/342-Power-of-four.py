# Problem: Leetcode 342 - Power of four
# Difficulty: Easy
# Link: https://leetcode.com/problems/power-of-four/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: We just check via both methods that the number has only 1 bit set 
# and with the mast we check that this set bit is in an even position because if its in odd positions
# then those powers of 2 are not divisible by 4.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
    
        return n>0 and n&(n-1)==0 and n&0xAAAAAAAA == 0
        '''
        usual solution
        b = bin(n)[2:]
        if n.bit_count()==1 and b.count('0')%2==0:
            return True
        return False
        '''