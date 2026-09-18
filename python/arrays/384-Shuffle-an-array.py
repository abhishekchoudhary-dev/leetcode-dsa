# Problem: Leetcode 384 - Shuffle an array
# Difficulty: Medium
# Link: https://leetcode.com/problems/shuffle-an-array/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We can generate the permutations and then select a random integer and return it which will return a random permutation.
# but unfortunately that will not find the answer as this is very big computationally. So we have to know the fisher yates algorithm
# which will help us generate a random permutation while only in O(n) by going over the array


import random
class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.og = self.nums[:]
        self.permutations = []
        #self.permute(nums)
        

    def reset(self) -> list[int]:
        self.nums = self.og[:]
        return self.nums

    def permute(self,nums):
        def backtrack():
            if len(sol) ==len(nums):
                self.permutations.append(sol[:])
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
    
        sol = []
        backtrack()
        

    def shuffle(self) -> list[int]:
        #fisher yates
        arr = self.nums[:]
        for i in range(len(arr)-1,0,-1):
            j = random.randint(0,i)
            arr[j],arr[i] = arr[i], arr[j]
        return arr


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()