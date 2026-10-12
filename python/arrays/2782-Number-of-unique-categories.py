# Problem: Leetcode 2782 - Number of unique categories
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-unique-categories/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: So the concept is that the actual array is part of the API and is hidden and a and b are the indices
# so we keep a main set and keep adding new elements to the set and then each for each index we pass the 
# previous seen index and check that values on those indices are same and if yes we increment our count
# we could also instead of set just run a nested loop where each index is checked against all indices for 0 to the current to
# find repetitions

# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass

from typing import Optional
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        unique = set()
        cnt = 0
        for i in range(n):
            new_category = True
            for val in unique:
                if categoryHandler.haveSameCategory(val,i):
                    print("checking",val,i)
                    new_category = False
                    break
            if new_category:
                unique.add(i)
                cnt+=1
        return cnt