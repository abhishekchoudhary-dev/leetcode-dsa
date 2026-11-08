
# Problem: Leetcode 4107 - Count valid suffix sorts I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-valid-suffix-sorts-I/description/
# Time Complexity: O(n) as we loop twice but its O(n) + O(n) so still O(n)
# Space Complexity: O(1)
# Approach: We find the index where the non decreasing order breaks in target and call this first_true_index. 
# Then we loop over nums and if we find that nums[i] and target[i] is not equal and i < first_true_index we immediately return 
# - as then nums cannot be made equal to target. Otherwise we keep continuing and past the first_true_index and if at any point nums[i] and target[i] is not equal then we 
# immediately stop as beyond this index we will not be able to make nums and target equal and this is the last index where we have change to find equality and every index
# between first_true_index and stop_index would be valid. But we need to test the stop_index at the end to see if its valid itself. If it fails then we return 0 again as it means 
# any index before stop_index and between first_true and stop cannot make nums equal to target and if it is possible then it means any index between first_true_index and stop_index 
# inclusive will be able to make nums equal to target. so then we return stop_index - first_true_index + 1


class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        first_true_index= 0
        for i in range(len(target)-2, -1,-1):
            if target[i] < target[i+1]:
                first_true_index = i+1
                break
        stop_index=len(nums)-1
        for i in range(len(nums)):
            if nums[i] != target[i] and i < first_true_index:
                return 0
            if nums[i]!=target[i]:
                stop_index=i
                break
        if nums[:stop_index] + sorted(nums[stop_index:],reverse=True) != target:
            return 0
        return stop_index - first_true_index+1
    