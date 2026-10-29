# Problem: Leetcode 3882 - Minimum XOR path in the grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/Minimum-XOR-path-in-the-grid/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only keep last state
# Approach: We are using dynamic programming but the main idea is that XOR is not monotonics in any way
# so the solution below is trying to keep track of the maximum number of same bits and take that path to achieve a xor sum
# as close to 0 as possible as same bits become 0. But this does not work with xor. We would rather need dp states like
# dp[i][j][v] with v keep a true false to check if that particular value is reachable or not. Hence we make a more optimized solution
# where we take dp states as set for each row of matrix. we start from initial value and then if it on the first row and col
# we just skip. otherwise we take grip cell value and by using set union we find the all reachable values
# as dp[j] from previous iteration is saving all the reachable values. then new dp[j] is built in this way
# that it xor's everything in reachable meaning all reachable values with the current grid value to find the new set of everything that is reachable
# so basically till the end we are tracking all possible values and then we return min(dp[-1)]) to return 
# the min value reached in the last row of the set
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dp = [set() for _ in range(cols)]
        dp[0].add(grid[0][0])
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    continue
                value = grid[i][j]
                reachable = dp[j] | (dp[j-1] if j>0 else set())
                dp[j] = {k^value for k in reachable} #take all possible values
                #basically this is the way to take all possible values in efficient way
                #no condition with XOR
            
        return min(dp[-1])

        '''
        # cannot use this greedy approach of tracking xor as its Non monotonic in every way
        def count_same_bits(a,b):
            #print("same bits between",a,b,"Are",sum(((a >> i) & 1) == ((b >> i) & 1) for i in range(max(a.bit_length(), b.bit_length()))))
            return sum(((a >> i) & 1) == ((b >> i) & 1) for i in range(max(a.bit_length(), b.bit_length())))
        rows , cols = len(grid), len(grid[0])
    
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0]=grid[0][0]  #initialize
        for i in range(1,len(grid[0])):
            dp[0][i] = grid[0][i]^dp[0][i-1]
        for i in range(1,len(grid)):
            dp[i][0]=grid[i][0]^dp[i-1][0]
        #now start finding
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                first = count_same_bits(dp[i-1][j], grid[i][j])
                second = count_same_bits(dp[i][j-1],grid[i][j])
                if first==second:
                    dp[i][j] = grid[i][j]^(dp[i][j-1] if grid[i][j]^dp[i][j-1] < grid[i][j]^dp[i-1][j] else dp[i-1][j])
                else:
                    dp[i][j] = grid[i][j] ^ (dp[i-1][j] if count_same_bits(dp[i-1][j], grid[i][j]) > 
                    count_same_bits(dp[i][j-1],grid[i][j]) else dp[i][j-1])
        return dp[rows-1][cols-1]

        '''