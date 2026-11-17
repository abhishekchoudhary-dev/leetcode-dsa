import java.util.*;
/* 
# Problem: Leetcode 3708 - Longest fibonacci subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-fibonacci-subarray/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: While this is a simple two pointer increment problem this question has taught me something very important. 
# the execution of code is not straightforward even when the BigO complexity is same. 
# two nested while loops have manual indexing constrains and multiple paths evven when i gets updated to j and it loos liek O(n).
# but one for loop with a curr varibale is one path forward which is straight. So for JVM JIT compiler this indexing
# with i=j becomes complicated to handle vs one curr variable. Also the CPU path with one variable is more predictable
# also using max specially with python version calls python max function again and again and makes it slow. the if 
# check for max is much faster. 
# now main thing is MEMORY - just one counter variable - the JVM and CPU can keep it inside the memory and the CPU.
# but repeated indexing arithmetic with array out of bounds check is much more complicated for memory.

*/ 


class Solution {
    public int longestSubarray(int[] nums) {
        int curr = 2;
        int mx = 2;
        for(int i=2;i<nums.length;i++){
            if (nums[i] == nums[i-1] + nums[i-2]){
                curr++;
                if (curr>mx) mx = curr;
            }
            else curr=2;
        }
        return mx;
    }
        /*
        int i =0;
        int mx=2;
        while(i<nums.length-1){
            int j = i+1;
            while(j+1 < nums.length && nums[j+1] == nums[j]+nums[j-1]){
                j++;
            }
            mx = Math.max(mx,j-i+1);
            i=j;
        }
        return mx;
    }*/

    
}
