WITH salarys AS (
    SELECT DISTINCT salary
    FROM employee
),
ranked AS (
    SELECT salary,
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM salarys
)
SELECT salary
FROM ranked
WHERE rn = 3;