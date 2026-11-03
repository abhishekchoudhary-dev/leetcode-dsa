package Java.hashmap;
import java.util.*;
/* 
# Problem: Leetcode 2284 - Sender with largest word count
# Difficulty: Medium
# Link: https://leetcode.com/problems/sender-with-largest-word-count/description/
# Time Complexity: O(n) - as we go through all the elements to make hashmap and then iterate the hashmap
# Space Complexity: O(n) as we use a hashmap
# Approach: We store the count in hashmap and then iterate it to find the max value and take the keys out that have this value
# then we just sort it and return lexicographically the biggest key
*/


class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        Map<String,Integer> map = new HashMap<>();
        int track = 0;
        for(String message : messages){
            String[] values = message.split(" ");
            map.put(senders[track],map.getOrDefault(senders[track],0)+values.length);
            track++;
        }
        int mx = 0;
        for(Integer value: map.values()){
            mx = Math.max(mx,value);
        }
        List<String> ans = new ArrayList<>();
        for(Map.Entry<String,Integer> entry: map.entrySet()){
            if (entry.getValue() == mx){
                ans.add(entry.getKey());
            }
        }
        Collections.sort(ans);
        return ans.get(ans.size()-1);

    }
} {
    
}
