# Problem: Leetcode 1882 - process tasks using servers
# Difficulty: Medium
# Link: https://leetcode.com/problems/process-tasks-using-servers/description/
# Time Complexity: O(n log n)
# Space Complexity: O(n) as we two hashmaps and a separate one to keep check on distances to avoid nested loops as that wont work
# Approach: There is a logical second solution which becomes TLE where i keep a busy array and assign the task and if all are busy
# then task is already assigned to the server which will get free first as they are already sorted by weight and index in server_id array.
# But since for every task we have to find a suitable server and the servers are dynamic and keep changing , this is perfect fit for a heap
# so we convert free and busy into a heap and then we can find suitable server in O(log n) time.

from collections import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w,i) for i,w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        t = 0
        for i, dur in enumerate(tasks):
            t = max(t,i)
            if not free:
                t = max(t,busy[0][0])
            while busy and busy[0][0] <= t:
                _,w,idx = heapq.heappop(busy)
                heapq.heappush(free,(w,idx))
            w , idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (t+dur , w, idx))
        return ans
        '''
        Fully working solution TLE
        # but this is the thing that if the thing being searched is constantly changing
        # and evolving then reach for a heap

        server_ids = sorted(range(len(servers)), key= lambda x: servers[x])
        busy_till = [0]*len(servers)
        ans = [0]*len(tasks)
        for i,time in enumerate(tasks):
            all_busy = True
            earliest_free = float('inf')
            for server in server_ids:
                if busy_till[server] < earliest_free:
                    earliest_free = busy_till[server]
                    target_server = server
                if busy_till[server] <= i:
                    busy_till[server] = i+time
                    ans[i] = server
                    all_busy = False
                    break
            if all_busy:
                ans[i] = target_server
                busy_till[target_server] += time
                
        return ans 
        '''