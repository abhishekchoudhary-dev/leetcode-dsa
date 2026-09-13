# Problem: Leetcode 825 - Friends of appropriat ages
# Difficulty: Medium
# Link: https://leetcode.com/problems/friends-of-appropriate-ages/description/
# Time Complexity: O(n) but O(1) as we have fixed number of iterations
# Space Complexity: O(1) as we used a fixed size array
# Approach: We simply use a frequency array which reduced our work quite a lot as we only have to iterate over the ages
# and send a request to a target age if criteria matches. Then we can even have nested loops as it just works due to fixed number of iterations 
# of the nested loops which is 120 and 120.
# Approach2: We can brute force it easily but that leads to TLE
# Appraoch3: We can sort the ages and binary search the cut off point where the 0.5*ages[i]+7 lands and then everyone before that and between the sending persons index
# can be sent a friend request by the person. But we need to have a freq counter and prefix sum keeping track of how many people before current person have same age as
# in that case the request can be sent backwards also. Freq array is the smallest and easiest solution

from bisect import bisect_left
from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121  
        for age in ages:
            count[age] += 1

        total = 0
        for age_x in range(1, 121):
            if count[age_x] == 0:
                continue
            for age_y in range(1, 121):
                if count[age_y] == 0:
                    continue
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                if age_x == age_y:
                    total += count[age_x] * (count[age_x] - 1)
                else:
                    total += count[age_x] * count[age_y]
        return total
        '''
        ages.sort(reverse=True)
        cnt = 0
        def custom_search(arr,val) -> int:
            left = 0
            right = len(arr)-1
            while left < right:
                mid = (left+right)//2
                if arr[mid] >= val:
                    left = mid+1
                elif arr[mid] < val:
                    right = mid
            return left
        neg_ages = [-x for x in ages]
        for i in range(len(ages)):
            cut_idx = bisect_left(neg_ages, -(0.5*ages[i] + 7))
            if cut_idx > i:
                cnt += max(cut_idx-i-1,0)
            j=i
            same_age_valid = ages[i] > 0.5*ages[i] + 7
            while j > 0 and ages[j] == ages[j-1]:
                j-=1
                if same_age_valid:
                    cnt+=1
        return cnt
        '''

        '''
        pruned version but still TLE
        ages.sort(reverse=True)
        cnt = 0
        for i in range(len(ages)):
            for j in range(i+1,len(ages)):
                if ages[j] <= 0.5*ages[i] + 7:
                    break
                else:
                    if ages[i]==ages[j]:
                        cnt+=2
                    else:
                        cnt+=1
                
        return cnt
        '''
        '''
        brute force simulation- words but TLE
        def check_criteria(x,y):
            if y <= (x*0.5) + 7 or y > x or (y>100 and x<100):
                return False
            return True
        for i in range(len(ages)):
            for j in range(len(ages)):
                if j == i:
                    continue
                if check_criteria(ages[i],ages[j]):
                    cnt+=1
        return cnt
        '''