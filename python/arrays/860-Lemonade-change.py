# Problem: Leetcode 860 - Lemonade change
# Difficulty: Easy
# Link: https://leetcode.com/problems/lemonade-change/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: When customer gives a bill we keep variable for each type of bill and increment its count. But before incrementing we check if we can return
# change to the customer. Fives are most important so we try to return change will 10s first. If someone gives a 10 and we have no 5s then we return False
# twenties is more tricky where we checking if we have either at least 1 ten and 1 fives or 0 ten and 3 fives. if we dont we return false
# otherwise when we return changes we use a 10 first instead of two fives as 5 is more valuable. So while returning if we have a ten we return ten plus 5 and 
# if ten count is 0 then we return 3 fives.

from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = twentys = 0
        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                if fives == 0:
                    return False
                tens+=1
                fives-=1
            else:
                if (tens == 0 and fives<3) or fives==0:
                    return False
                twentys+=1
                if tens>0:
                    tens-=1
                    fives-=1
                else:
                    fives-=3
        return True   