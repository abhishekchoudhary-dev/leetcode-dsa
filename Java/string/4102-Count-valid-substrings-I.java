/* 
Problem: Leetcode 4102 - Count valid substrings I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-valid-substrings-I/description/
# Time Complexity: O(n) 
# Space Complexity: O(n)
# Approach: We count the valid substrings by keeping going forward with our pointer till we encouter a c which follows an a and b which means abc has been found in this substring
# then taken all substring is bad because its hard to calculate how many of them will have abc. so we take the substring legnth till previous index of c
# and then we take all the substring there but here is the tricky part. we set the prev pointer to i-1 to include all the substring from 'b' but this means that when 
# we took all the subtring between prev and i-1(as 'c' was a i) we need to substract 1 from the total as the substring 'b' will repeat otherwise
# increasing the total count. And ofcourse the substring are caclculated by the formula n*n+1//2
*/
class Solution {
    public long countValidSubstrings(String s) {
        long prev = 0;
        int i = 0;
        long total = 0;
        while (i<s.length()){
            if (i>1 && s.charAt(i)=='c'){
                if (s.charAt(i-1)=='b' && s.charAt(i-2)=='a'){
                    long length = i - 1 - prev + 1;
                    total += (length * (length+1))/2 - 1;
                    prev = i-1;
                }
            }
            i++;
        }
        long remaining = s.length() - prev;
        total += remaining * (remaining+1)/2;

        
        return total;
    }
} {
    
}
