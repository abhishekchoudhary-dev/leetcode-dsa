/*
# Problem: Leetcode 2855 - Minimum right shifts to sort the array
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimun-right-shifts-to-sort-the-array/description/
# Time Complexity: O(n^2) for slicing approach and O(n) for normal approach
# Space Complexity: O(n) for approach2 and O(1) for normal approach
# Approach1: we simply check the number of drops which should only be 1 if array can be rotates and sorted
# if its more than 1 we return -1 and if 0 we return 0 and otherwise we return length of array - rotation index
*/

import java.util.Collections;
import java.util.*;

class Solution {
    public int minimumRightShifts(List<Integer> nums) {

        int outOfPlace = 0;
        int rotationIndex = 0;
        for (int i=0;i<nums.size();i++){
            if (nums.get(i) > nums.get((i+1)%nums.size())){
                outOfPlace++;
                rotationIndex = (i+1)%nums.size();
            }
        }
        if (outOfPlace==0) return 0;
        if (outOfPlace>1) return -1;
        return (nums.size() - rotationIndex)%nums.size();

        /*
        int[] arr = nums.stream().mapToInt(x->x).toArray();
        System.out.println(Arrays.toString(arr)); //make in array
        int n = arr.length;
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        for (int i=0;i<arr.length;i++){
            boolean ok = true;
            for(int j=0;j<arr.length;j++){
                if (arr[(i+j)%n]!=sorted[j]) {ok = false; break;}
            }
            if(ok) return (n-i)%n;
        }
        return -1;
        
        ----with copy version------
        if (Arrays.equals(sorted,arr)) return 0;
        for(int i=0; i<arr.length; i++){
            int[] slice1 = Arrays.copyOfRange(arr,i,n); 
            int[] slice2 = Arrays.copyOfRange(arr,0,i);
            int[] result = Arrays.copyOf(slice1, slice1.length+slice2.length);
            System.arraycopy(slice2,0,result,slice1.length,slice2.length);
            //source -> source start, dest->dest start
            if (Arrays.equals(result,sorted)) return n-i;
        }
        return -1;
        
        List<Integer> sorted = new ArrayList<>(nums);
        Collections.sort(sorted);
        int n = nums.size();
        if (sorted.equals(nums)) return 0;
        for (int i=0;i<nums.size();i++){
            List<Integer> temp = new ArrayList<>(nums.subList(i,n));
            temp.addAll(nums.subList(0,i));
            //cannot do it in one step as usually subList is a copy in java 
            // so we make a new list by passing it to List<Integer> constructor
            //and then addAll() returns boolean so we call it separately
            if (temp.equals(sorted)) return n-i;

            //java sublist returns a view of list unlike python which
            //makes new list
        }


        return -1;
        */
    }
}