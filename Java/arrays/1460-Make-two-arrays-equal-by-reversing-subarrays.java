package Java.arrays;

/* 
# Problem: Leetcode 961 - N repeated element in size 2N arrat
# Difficulty: Easy
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2N-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: We just check for the first repeated value and we immediately return. we can have a final return 0 or throw a runtTime exception if 
# if the code flow reaches there as it was not supposed to.
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
