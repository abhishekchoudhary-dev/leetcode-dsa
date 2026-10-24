
#Problem: Leetcode 2409 - Count number of days spent together
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-number-of-days-spent-together/description/
# Time Complexity: O(n) as we construct prefix array
# Space Complexity: O(1)
# Approach: Question becomes easlier once we convert everything in total number of days and then we know which number is the day both arrived on 
# and departed on and we can just check overlap with simple math.

from datetime import date
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        alice_arrive_month, alice_arrive_date = arriveAlice.split("-")
        alice_depart_month,alice_depart_date = leaveAlice.split("-")
        bob_arrive_month, bob_arrive_date = arriveBob.split("-")
        bob_depart_month, bob_depart_date = leaveBob.split("-")
        prefix = [0]
        for days in days_per_month:
            prefix.append(days+prefix[-1])

        alice_arrive_day = prefix[int(alice_arrive_month)-1] + int(alice_arrive_date)
        alice_leave_day = prefix[int(alice_depart_month)-1] + int(alice_depart_date)
        bob_arrive_day = prefix[int(bob_arrive_month)-1] + int(bob_arrive_date)
        bob_leave_day = prefix[int(bob_depart_month)-1] + int(bob_depart_date)
        return max(0,min(alice_leave_day,bob_leave_day) - max(alice_arrive_day,bob_arrive_day)+1)
            


        '''
        #using date time
        alice_start_date = date(2026,int(alice_arrive_month),int(alice_arrive_date))
        bob_start_date = date(2026,int(bob_arrive_month),int(bob_arrive_date))
        alice_end_date = date(2026,int(alice_depart_month),int(alice_depart_date))
        bob_end_date = date(2026, int(bob_depart_month), int(bob_depart_date))
        overlap_start = max(alice_start_date,bob_start_date)
        overlap_end = min(alice_end_date,bob_end_date)
        if overlap_start <= overlap_end:
            return (overlap_end - overlap_start).days +1
        return 0
        '''