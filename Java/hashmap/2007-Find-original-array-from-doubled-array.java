package Java.hashmap;
import java.util.*;
/* 
# Problem: Leetcode 2007 - Find original array from doubled array
# Difficulty: Medium
# Link: https://leetcode.com/problems/finding-original-array-from-doubled-array/description/
# Time Complexity: O(n) - as we count frequencies and iterate over it
# Space Complexity: O(n) as we use a hashmap
# Approach: Important question to learn since I forgot about keeping freq with hashmap. General hashmap or set does not work
# as there is repetition so set cannot track and hashmap key value get overwritten. so only way is to keep freq
# in hashmap keys and to keep updating it
*/

class Solution {
    public int[] findOriginalArray(int[] changed) {
        if (changed.length%2==1) return new int[0];
        Arrays.sort(changed);
        Map<Integer,Integer> map = new HashMap<>();
        for(int num: changed){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        int write = 0;
        int[] original = new int[changed.length/2];
        for (int num: changed){
            if (map.containsKey(num) && map.get(num)>0){
                map.put(num,map.get(num)-1);
                int twice= num*2;
                if(map.containsKey(twice) && map.get(twice)>0){
                    map.put(twice,map.get(twice)-1);
                    original[write++] = num;
                }
                else return new int[0];
            }
        }
        return original;
    }
} {
    
}
