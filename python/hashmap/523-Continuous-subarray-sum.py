# Problem: Leetcode 523 - Continuous subarray sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-subarray_sum/description/
# Time Complexity: O(n) as we go through the array once
# Space Complexity: O(n) as we use a hashmap
# Approach: If we have to manually check all the element as we see in the brute force approach that any of then produce a diff from our running prefix sum
# which is a multiple of k then it causes TLE. So we just make a hashmap of remainders seen. and if a remainder has been seen before and is seen again now and both 
# of them has index difference > 1 meaning tthat subarray has length >2 we just return True. Also we update hashmap only when new remainder is seen
# otherwise we keep the first occurence of each remainder so that subarray can be largest and we dont accidently miss our on finding a subarray which. can return true.

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {0:-1}
        curr_sum = 0
        for i,num in enumerate(nums):
            curr_sum+=num
            remainder = curr_sum%k
            if remainder in d and i - d[remainder] > 1:
                return True
            if remainder not in d:
                d[remainder] = i
        return False
        '''Brute force TLE
        if len(nums)==1:
            return False
        if k==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] ==0:
                return True
        d = {0:-1}
        curr_sum = 0
        for i,num in enumerate(nums):
            curr_sum += num
            temp = curr_sum
            mul=1
            while temp-(k*mul)>=0:
                if temp-(mul*k) in d and i-d[temp-(mul*k)] > 1:
                    return True
                mul+=1
            if curr_sum not in d:
                d[curr_sum] = i
            

        return False
        '''
            