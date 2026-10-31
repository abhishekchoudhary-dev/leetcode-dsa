/* 
Problem: Leetcode 2220 - Minimum bit flips to convert number
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
# Time Complexity: O(k) where k is the max number of bits between start and goal
# Space Complexity: O(1)
# Approach - We just xor both which will find the different bits and then calculate the number of different bits
# We can also convert both to string the binary representations of the two numbers
# Approach2 - We use brian kerningham algorithm, where we keep doing & with number and number - 1 which will keep setting the LSB 1 to 0
# and end up with 0000000 all zeros. so the number of 1 bits(which were diff after xor) need to be set to 0
# so we can keep doing this in a loop and increment count before the xor goes to zero.
*/

class Solution {
    public int minBitFlips(int start, int goal) {
        //we can also use brian kerningham to have the trick
        //where you AND with number and number - 1 to set the LSB of 1 to 0
        //so if we just find how many times we set bit to 0 then it will work
        int xor = start ^ goal;
        int cnt = 0;
        while(xor!=0){
            xor &= xor-1; //till the time they keep getting set meaning xor has not become 0
            cnt ++;     
        }

        return cnt;

        /* - this is standard xor trick
        int xor  = start ^ goal;
        int cnt = 0;
        while (xor!=0){
            //int curr_bit = xor%10; //checking decimal version so no use
            //if (curr_bit==1) cnt++;
            if ((xor & 1)==1) cnt++;
            xor>>=1;
        }
        return cnt;
        */

    }
}