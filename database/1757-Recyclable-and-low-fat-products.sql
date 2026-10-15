-- Problem: Leetcode 1757 - Recyclable and low fat products
-- Difficulty: Easy
-- Link: https://leetcode.com/recyclable-and-low-fat-products/description/
-- Approach: We simply just choose product id where low fact and recyclables act like the target
-- because enum behaves like normal column itself but just ensures data integrity

select product_id 
from Products
where low_fats = 'Y' and recyclable = 'Y';