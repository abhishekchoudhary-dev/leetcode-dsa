
# Problem: Leetcode 453 - Minimum moves to equal array elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space used
# Approach: Since we are mandated to take n-1 elements every time we have to realize that 
# the smallest element has to close the gap to each bigger element individually and that is what we do

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves = 0
        #nums.sort() - avoid sorting
        smallest = min(nums)
        for num in nums:
            moves += (num - smallest) #min element will have to close up all the distances
        return moves

        '''
        if len(nums)==1 or len(set(nums))==1:
            return 0
        nums.sort()
        mx_index = -1
        mx_value = nums[mx_index]
        moves = 0
        smallest = nums[0]
        while smallest!=mx_value:
            moves += (mx_value -  smallest)
            smallest+=moves
            mx_index-=1
            mx_value = nums[mx_index] + moves
            print("mx_index is", mx_index)
            print(smallest,mx_value)
        
        return moves
        '''
