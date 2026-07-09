-- Last updated: 7/9/2026, 3:07:45 PM
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;