import java.util.*;
/* 
# Problem: Leetcode 1403 - Minimum subsequence in non increasing order
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/
# Time Complexity: O(n log n) as we have to sort the array multiple times for reversing
# Space Complexity: O(1) as no extra data structure used
# Approach: The requirement are complicated but main idea is to realize that since we have to return the smallest length of all possible subsequences 
# which will have sum greater than remaining then it can only include the bigger numbers. So we just reverse sort the array
# and loop on it to find the index where we should cut as soon as sum exceeds sum from the remaining elements.
# then we cut it and return that first part of reversed array
*/
class Solution {

    private int[] reverseSort(int[] arr){
        for(int i=0; i < arr.length/2;i++){
            int temp = arr[i];
            arr[i] = arr[arr.length-i-1];
            arr[arr.length-i-1] = temp;
        }
        return arr;
    }
    public List<Integer> minSubsequence(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        sorted = reverseSort(sorted);
        int total = 0;
        for (int num: nums) total+=num;
        int currSum = 0;
        int cutIndex = 0;
        for (int i=0;i<sorted.length;i++){
            currSum+=sorted[i];
            if (currSum > total - currSum){
                cutIndex = i;
                break;
            }
        }
        int[] ans = Arrays.copyOfRange(sorted,0,cutIndex+1);
        Arrays.sort(ans);
        ans = reverseSort(ans);
        List<Integer> list = Arrays.stream(ans).boxed().collect(Collectors.toList());
        return list;
    }
}