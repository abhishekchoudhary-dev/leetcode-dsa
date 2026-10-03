/* 
# Problem: Leetcode 3411 - Maximum subarray with equal products
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-subarray-with-equal-products/description/
# Time Complexity: O(n^2) + prefix to avoid an O(n^3) loop
# Space Complexity: O(n) as we calculate prefix sums
# Approach: We have to calculate the lcm and gcd of each subarray so to avoid O(n^3) loop we calculate the product of the subarray
# by precalculating the prefix product and then we can calcutate the product in O(1) time and gcd and lcm are calulated using in build functions.
# then we keep updating our best variable to hold the best possible answer.  To void overflow
# we are using BigInteger. Also we need to calculate all of gcd and lcm manually as java does not have in built support for these thigns.
*/ 

package Java.arrays;

import java.util.Arrays;
import java.math.BigInteger;
class Solution {
    public static int gcd(int a,int b){
        while(b!=0){
            int remainder =a%b;
            a = b;
            b = remainder;
        }
        return a;
    }
    public static int lcm(int a, int b){
        return a*b / gcd(a,b);
    }
    public static int find_gcd(int[] arr){
        int gcd = arr[0];
        for (int i=1;i<arr.length;i++){
            gcd = gcd(gcd,arr[i]);
        }
        return gcd;
    }
    public static int find_lcm(int[] arr){
        int lcm = arr[0];
        for(int i = 1;i<arr.length;i++){
            lcm = lcm(lcm,arr[i]);
        }
        return lcm;
    }
    public int maxLength(int[] nums) {
        int best = 0;
        //int[] prefix = new int[nums.length+1];
        //prefix[0] = 0;
        //int prod = 1;
        //for (int i = 0; i < nums.length;i++){
        //    prod*=nums[i];
        //    prefix[i+1] = prod;
        //}
        BigInteger[] prefix = new BigInteger[nums.length + 1];
        prefix[0] = BigInteger.ONE;

        BigInteger prod = BigInteger.ONE;

        for (int i = 0; i < nums.length; i++) {
            prod = prod.multiply(BigInteger.valueOf(nums[i]));
            prefix[i + 1] = prod;
        }
        for (int i=0;i<nums.length;i++){
            for (int j=i;j<nums.length;j++){
                int[] sub = Arrays.copyOfRange(nums,i,j+1);
                int g = find_gcd(sub);
                int l = find_lcm(sub);
                //int p = 1;
                BigInteger p = prefix[j + 1].divide(prefix[i]);

                if (p.equals(BigInteger.valueOf((long) g * l))) {
                    best = Math.max(best, j - i + 1);
                }
                //if (prefix[i]!=0) p = prefix[j+1]/prefix[i];
                //else p = prefix[j+1]-prefix[i];
                //if (p==(g*l)){
                //    best = Math.max(best,j-i+1);
                //}
            }
        }
        return best;
    }
}
