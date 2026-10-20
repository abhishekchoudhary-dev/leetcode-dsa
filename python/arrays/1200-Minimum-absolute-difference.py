# Problem: Leetcode 1200 - Minimum absolute difference
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-absolute-difference/description/
# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(n) but only for answer array
# Approach: We traverse the array once and we find the mn difference breaking early if we find one. We first sort the array
# so that the mn difference if found early. THen we make a single loop to find the possible paiars and we only check the next element of each element
# because the realization is that if the next element of any element has a diff less than min then thats not possible as it would have been minimum itself
# and otherwise if its bigger than nothing to the right of the next element can make a valid pair.
# so we only check the next element and if diff is equal of min we just take them in our answer array.

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        mn = float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            mn = min(mn,arr[i+1]-arr[i]) #find min diff
            if mn==1:
                break
        ans = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == mn:
                ans.append([arr[i],arr[i+1]])
        return ans