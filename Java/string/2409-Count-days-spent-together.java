/* 
Problem: Leetcode 2409 - Count number of days spent together
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-number-of-days-spent-together/description/
# Time Complexity: O(n) as we construct prefix array
# Space Complexity: O(1)
# Approach: Question becomes easlier once we convert everything in total number of days and then we know which number is the day both arrived on 
# and departed on and we can just check overlap with simple math.
*/

import java.util.*;
class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        List<Integer> prefix = new ArrayList<>();
        prefix.add(0); //inside brackets its capacity
        List<Integer> daysInMonths = List.of(31,28,31,30,31,30,31,31,30,31,30,31);
        for (Integer days: daysInMonths){
            prefix.add(prefix.get(prefix.size()-1) + days);
        }
        int aliceArriveDay = calculateDay(arriveAlice, prefix);
        int aliceLeaveDay = calculateDay(leaveAlice, prefix);
        int bobArriveDay = calculateDay(arriveBob,prefix);
        int bobLeaveDay = calculateDay(leaveBob,prefix);
        return Math.max(0, Math.min(aliceLeaveDay, bobLeaveDay)- Math.max(aliceArriveDay, bobArriveDay)+1);

    }

        private static int calculateDay(String date, List<Integer> prefix){
            int month = Integer.parseInt(date.substring(0,2));
            int day = Integer.parseInt(date.substring(3,date.length()));
            return prefix.get(month-1) + day;
        }
    
} {
    
}
