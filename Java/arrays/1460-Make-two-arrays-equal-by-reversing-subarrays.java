package Java.arrays;

/* 
# Problem: Leetcode 1460 - Make two arrays equal by reversing subarrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) depending on what type of internal sort is used
# Approach: Since all types of swapping is allowed we basically have to check parity of starting and target array.
# If they have equal parity then we can say that target can be achieved since any pair can be shuffled.
*/
import java.util.*;
class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        Arrays.sort(arr);
        Arrays.sort(target);
        return Arrays.equals(arr,target);
    
        /*
        HashMap<Integer,Integer> a = new HashMap<>();
        HashMap<Integer,Integer> t = new HashMap<>();
        for (int num:arr){
            a.put(num,a.getOrDefault(num,0)+1);
        }
        for (int num:target){
            t.put(num,t.getOrDefault(num,0)+1);
        }
        for(Map.Entry<Integer,Integer> e: a.entrySet()){
            if (!t.containsKey(e.getKey()) || !(e.getValue().equals(t.get(e.getKey())))) return false;
        }
        return true;
    }
    */
    }
} {
    
}
