# Problem: Leetcode 1520 - Maximum number of non overlapping substrings
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/
# Time Complexity: O(n log n) as we sort the intervals
# Space Complexity: O(n) as we use separate hashmaps for first and last
# Approach: We take the first and last occurence of all characters in two hashmaps and then in a loop
# for every character's first and last occurence we check that all characters between its first and last occurence (if they occur or maybe they done and current character repeats)
# we increment our index. if a window of a characters start and end index is found to be valid we take into into intervals.
# then we sort intervals with x[1] and if last occurence of two intervals is same then by their length as smallest interval should come first
# then we just go over intervals and add those which dont overlap

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c, start in first.items():
            end = last[c]
            j = start
            valid = True
            while j <= end:
                cj = s[j]
                if first[cj] < start:
                    valid = False
                    break
                end = max(end, last[cj])
                j += 1
            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        ans = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end+1])
                prev_end = end
        return ans
        '''
        #greedy single substring will always be better
        last_idx = {char:idx for idx,char in enumerate(s)}
        print(last_idx)
        prefix = [0]*len(s)
        unique = set()
        for i,char in enumerate(s):
            unique.add(char)
            prefix[i] = len(unique)
        print(prefix)
        left = 0 
        ans = []
        seen = set()
        d = {} 
        right = 0
        while right < len(s):
            if right==last_idx[s[right]] and s[right] not in seen:
                ans.append(s[right]) #all occurrences guaranteed
            elif s[right] not in seen:
                start = right
                while right+1 < len(s) and s[right] == s[right+1]:
                    right+=1
                if right == last_idx[s[right]]:
                    ans.append(s[right]*(right-start+1))
            seen.add(s[right])
            right+=1
        
        if not ans:
            ans.append(s)
        return ans
        '''