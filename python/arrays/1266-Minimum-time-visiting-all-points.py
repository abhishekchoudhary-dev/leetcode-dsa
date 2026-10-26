# Problem: Leetcode 1266 - Minimum time visiting all points
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-time-visiting-all-points/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We have full long solution below where we always convert distance between two points into the positively sloped upwards sloping line 
# for clarity. However, there is smaller way where we just calculate take the max of differnece of x and y points between any two consecutive points
# because diagonal movement will come closer to the target points and then whichever points has more distance, that much extra time will be taken to move in t
# that particular direction which could be x or this could be y direction

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total = 0
        for i in range(len(points)-1):
            x1,y1 = points[i]
            x2,y2= points[i+1]
            total += max(abs(x2-x1),abs(y2-y1))
        return total

        '''
        def find_min_distance(p1,p2)->int:
            if p1[0] > p2[0]:
                p1,p2=p2,p1 #switch points
            p1_x,p1_y = p1
            p2_x,p2_y = p2
            if p1_x == p2_x: return abs(p1_y-p2_y) #mandatory straight line
            if p1_y == p2_y: return abs(p1_x-p2_x) #mandatory straight line
            #not straight line
            direct = abs(p1_x-p2_x) + abs(p1_y-p2_y)
            cnt = 0
            if p2_y < p1_y:
                p2_y = p1_y + abs(p1_y-p2_y) #always make positive slope
            while p1_x < p2_x and p1_y<p2_y:
                p1_x+=1
                p1_y+=1
                cnt+=1
            remaining = abs(p2_x - p1_x) + abs(p2_y-p1_y)
            return min(direct, cnt+remaining)
            

        total = 0
        prev_x,prev_y = points[0]
        for i in range(len(points)-1):
            total+=find_min_distance(points[i],points[i+1])
            
        return total
        '''