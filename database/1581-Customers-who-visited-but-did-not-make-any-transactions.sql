-- Problem: Leetcode 1581 - Customers who visited but did not make any transactions
-- Difficulty: Easy
-- Link: https://leetcode.com/customers-who-visited-but-did-not-make-any-transaction/description/
-- Approach: We basically just join the tables and take the rows that have no matching transaction id again their name
-- and then just group the remaining ones and count total rows of grouped ones

select v.customer_id,count(*) as count_no_trans
from Visits v
left join Transactions t
    on v.visit_id = t.visit_id
where t.transaction_id IS NULL
group by v.customer_id;
