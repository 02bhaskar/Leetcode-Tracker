-- Last updated: 7/9/2026, 3:07:47 PM
SELECT E2.name AS Employee
FROM Employee E1
JOIN Employee E2
    ON E1.id = E2.managerId
WHERE E2.salary > E1.salary;