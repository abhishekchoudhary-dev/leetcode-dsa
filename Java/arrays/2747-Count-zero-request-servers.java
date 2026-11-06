import java.util.*;
/* 
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
*/

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Arrays.sort(logs,Comparator.comparingInt(k->k[1]));
        Integer[] ids = new Integer[queries.length];
        for (int i=0;i<queries.length; i++){
            ids[i] = i;
        }
        Arrays.sort(ids, Comparator.comparingInt(k->queries[k]));
        //System.out.println(Arrays.deepToString(logs)+""+Arrays.toString(ids));
        int active = 0,left = 0,right = 0;
        int[] ans = new int[queries.length];
        int[] cnt = new int[n+1];
        for (int i : ids){
            int q = queries[i];
            while (right < logs.length && logs[right][1] <= q){
                int id = logs[right][0];
                if (cnt[id]==0){
                    active++;
                }
                cnt[id]++;
                right++;
            }
            while (left<right && logs[left][1] < q-x){
                int id= logs[left][0];
                cnt[id]--;
                if(cnt[id]==0) active--;
                left++;
            }
            ans[i] = n - active;
        }
        return ans;

    }
} 
