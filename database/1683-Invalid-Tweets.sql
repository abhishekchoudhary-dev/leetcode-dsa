-- Problem: Leetcode 1683 - Invalid tweets
-- Difficulty: Easy
-- Link: https://leetcode.com/invalid-tweets/description/
-- Approach: Extemely simple just showing us length function usage

select tweet_id
from Tweets
where CHAR_LENGTH(content) > 15;

-- LENGTH words as well