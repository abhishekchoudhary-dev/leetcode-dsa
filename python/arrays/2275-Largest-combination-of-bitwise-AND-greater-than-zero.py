# Problem: Leetcode 2275 - Largest combination of bitwise AND greater than zerp
# Difficulty: Medium
# Link: https://leetcode.com/problems/largest-combination-of-bitwise-AND-greater-than-zero/description/
# Time Complexity: O(n) for n elements in nums
# Space Complexity: O(1) as no extra data structure is used
# Approach: Since there is no monotonicity here the only way to check this is count a bit position that is set the maximum
# number of times as those many numbers can be picked up with that 1 bit set and result will be guaranteed to be 
# greater than 0. So we make a bit freq array and for each number we basically cnt the bits
# and then the answer is the maximum amount of set bit positions

class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        set_bits = [0]*32 #as integer is 32 bit
        for num in candidates:
            for bit in range(32):
                if num & 1<<bit:
                    set_bits[bit]+=1
        return max(set_bits)