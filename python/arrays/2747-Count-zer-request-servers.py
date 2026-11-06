
# Problem: Leetcode 2747 - Count zero request servers
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-zero-request-servers/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) as we make ans array, cnt freq array
# Approach: We sort logs with server time and then we sort queries to check server usage in a monotonic manner
# the catch is that if we sort queries directly then sequence is reuqired to add in the ans array and we need a hashmap to keep track of their original index
# we can keep a hashmap but thats additional steps. so we rather just sort the indices of query based on query values
# and then store in 'ids' and we will go over queries in correct order now rather than sorting queries separately
# and keeping a record of it in the hashmap. then we go over ids and then we get queries in correct sequence
# and then we move the window with left and right points and the main MAGIC is a frequencey array which will track the 
# active arrays which will update the count array and keep track of number of active servers in the current window
# since we are counting active ones the prefix system will not work.

# Approach 2 -we can sort the logs and then for each query we bisect left adn right and we find the indices on which the current query fits
# between q-x and q and then count the unique server in that but this is causing TLE

from typing import List
from bisect import bisect_left,bisect_right
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sorting + sliding window maybe??
        logs.sort(key=lambda x:x[1])
        ids = sorted(range(len(queries)), key=lambda i:queries[i])
        ans = [0] * len(queries)
        cnt = [0]*(n+1)
        left = right = active = 0
        for i in ids:
            q = queries[i]
            while right < len(logs) and logs[right][1] <= q:
                id = logs[right][0]
                if cnt[id] == 0:
                    active+=1
                cnt[id]+=1
                right+=1
            while left < right and logs[left][1] < q-x:
                id = logs[left][0]
                cnt[id]-=1
                if cnt[id] == 0:
                    active-=1
                left+=1
            ans[i] = n-active
        return ans





        '''
        this binary search appraoch doesnt work
        ans = []
        logs.sort(key=lambda x:x[1])
        end_times = [x[1] for x in logs]
        for q in queries:
            start,end = q-x,q
            left = bisect_left(end_times,start)
            right = bisect_right(end_times,end)
            temp = set()
            for i in range(left,right):
                temp.add(logs[i][0])
            ans.append(n-len(temp))
        return ans
            

        '''