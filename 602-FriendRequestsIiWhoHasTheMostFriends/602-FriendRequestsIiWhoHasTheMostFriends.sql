-- Last updated: 7/17/2026, 9:35:21 AM

WITH ids AS (
(SELECT
    accepter_id,
    COUNT(accept_date) AS num
FROM requestaccepted
GROUP BY accepter_id
)

UNION ALL

   (SELECT
   requester_id,
   (COUNT(accept_date) ) AS num
FROM requestaccepted
GROUP BY requester_id)
)

SELECT accepter_id AS id,
SUM(num) AS num
FROM ids
GROUP BY id 
ORDER BY num DESC LIMIT 1;