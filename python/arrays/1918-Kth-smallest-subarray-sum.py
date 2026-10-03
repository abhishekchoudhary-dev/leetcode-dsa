
# Problem: Leetcode 1918 - Kth smallest subarray sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-smallest-subarray-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: For subarray question if we cannot store in hashmap or prefix array and brute force is not allowed as in this question
# then alternate is almost always a binary search on the answer or some tree solution. Here we know that kth sum will be between minimum value of nums
# or the total sum of nums and we use this info to do a binary search on the answer. to do binary search we run a sliding window and then we see how
# many subarrays end at the index right and are they greater than k or not which means that the right index is enough meaining 
# that enough subarrays end at the mid index which have a sum less than k meaning that kth smallest sum will be in this range ofcourse
# if yes we can either take it in an answer variable or we can keep seartching and return the lo variable which will close on the answer
# Our function is used to find using a sliding window how many subarrays have sum less than mid and then in our main loop
# we check if this cnt is >=k because if it is then at this sum value we can find enough subarrays and the kth smallest value will lie in that range.

from sortedcontainers import SortedList
class Solution:
    def kthSmallestSubarraySum(self, nums: list[int], k: int) -> int:
        def bs(nums,k):
            #run window to see how many subarrays have this sum
            cnt = 0
            left = 0
            curr_sum = 0
            for right in range(len(nums)): #subarrays mein think sliding coz i have 
            # right-left+1 to count subarrays ending on the right side
                curr_sum+=nums[right]
                while curr_sum > k:
                    curr_sum-=nums[left]
                    left+=1
                cnt += right-left+1
            return cnt
        lo = min(nums)
        hi = sum(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if bs(nums,mid)>=k:
                hi = mid
            else:
                lo=mid+1
        return lo

        '''brute force idea - TLE
        sums = SortedList()
        prefix = [0]*(len(nums)+1)
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            prefix[i+1] = curr_sum
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums.add(prefix[j+1]-prefix[i])
        return sums[k-1]
        '''