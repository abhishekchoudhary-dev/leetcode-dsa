# Problem: Leetcode 4099 - Minimum operations to sort with locked indices
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-sort-with-locked-indices/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we do not use extra space
# Approach: Since input size is 2000 we can run a usual nested sorting loop like bubble sort 
# and before bubbling we keep chcking the posiitons being swapped so that if they are locked we increase the unlock count by 1
# if unlock count during loop exceeds k then we immediately return -1 else we keep going
# and at the end we return swaps + unlock

class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        swaps = 0
        unlocks = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    if locked[i]:
                        locked[i] = 0
                        unlocks+=1
                    if locked[j]:
                        locked[j] = 0
                        unlocks+=1
                    if unlocks>k:
                        return -1
                    swaps+=1
        return swaps+unlocks 
        ''' we dont need cycles. alternating swap we need
        arr_pos = sorted(range(len(nums)), key = lambda i: nums[i])
        #print(arr_pos)
        visited = [False]*len(nums)
        swaps = 0
        unlocks = 0
        for i in range(len(nums)):
            if visited[i] or i==arr_pos[i]:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                if locked[j]:
                    unlocks+=1
                    locked[j]=0
                visited[j] = True
                j = arr_pos[j]
                cycle_size+=1
            swaps+=cycle_size-1
        print(swaps, unlocks)
        return swaps+unlocks if unlocks<=k else -1
        '''