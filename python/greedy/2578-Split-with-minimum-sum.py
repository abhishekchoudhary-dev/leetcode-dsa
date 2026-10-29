# Problem: Leetcode 2578 - Split with minimum sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/split-with-minimum-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only use pointers
# Approach: We basically use greedy approach. Since both numbers need to have min sum
# there is only one option which is to keep both minimum and of that. the smallest digits should occupy
# the most significant bit positions so we basically sort the digits in increasing order and keep taking the digits 
# for each number alternatively so digit on even index we take for first number and on odd index for second
# which are already sorted so they guaranteee the minimum possible two numbers which in turn guarantees the 
# minimum sum


class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        s = sorted(s)
        first = []
        second = []
        for i in range(0,len(s)):
            if i%2==0:
                first.append(s[i])
            else:
                second.append(s[i])

        #first = s[0::2]
        #second = s[1::2]
        return int(''.join(first)) + int(''.join(second))