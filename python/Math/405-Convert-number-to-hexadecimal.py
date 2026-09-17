# Problem: Leetcode 405 - Convert number to hexadecimal
# Difficulty: Easy
# Link: https://leetcode.com/problems/convert-number-to-hexadecimal/description/
# Time Complexity: O(num//16)
# Space Complexity: O(1) as hexMap is already built
# Approach: We simply just break the number down by extracting each digit and putting it into hexadecimal array and then return the reverse of it
# But then for two's complement we do pure arithmetic convertsion of 2^n-num so we can do 2^32 + num since num is negative. 
# and then usual process of converting to hexadecimal follows. For negative nos we can also convert it to a full string of bits which we invert and add 1 to it
# by using the carry method to add 1 to string to converting string to int and then using a mask inverting it and adding while preventing overflow.
# direct arithmetic conversion is faster.


class Solution:

    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hexMap = "0123456789abcdef"
        if num < 0:
            num+= 1<<32
        hexa = []
        while num > 0:
            digit = num%16
            hexa.append(hexMap[digit])
            num //= 16
        return ''.join(reversed(hexa))