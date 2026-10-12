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