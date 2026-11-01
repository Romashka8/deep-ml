WITH ranked AS (
    SELECT department,
           name,
           salary,
           DENSE_RANK() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rn
    FROM employees
)
SELECT department, name, salary, rn
FROM ranked
WHERE rn <= 3;