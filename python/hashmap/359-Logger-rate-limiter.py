# Problem: Leetcode 359- Logger rate limiter
# Difficulty: Easy
# Link: https://leetcode.com/problems/logger-rate-limiter/description/
# Time Complexity: O(n)
# Space Complexity: O(1) for xor and O(n) for hashmap
# Approach: we can use simple hashmap and add add timestamp of the message if its new message or update the timestamp if old 
# and if a message arrives with a timestamp smaller than it then we return False

class Logger:

    def __init__(self):
        self.log = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log or timestamp >= self.log[message]:
            self.log[message] = timestamp+10
            return True
        elif timestamp < self.log[message]:
            return False
    
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)