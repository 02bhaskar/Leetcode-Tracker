-- Last updated: 7/17/2026, 9:35:20 AM
SELECT S.name
FROM SalesPerson S
WHERE S.sales_id NOT IN (
SELECT Orders.sales_id
FROM Orders
JOIN
Company ON
Orders.com_id = Company.com_id
where Company.name = 'RED')