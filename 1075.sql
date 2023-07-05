SELECT project_id, ROUND ( AVG(1.0 * experience_years) , 2) AS 'average_years'
FROM Employee E
FULL OUTER JOIN Project P on E.[employee_id] = P.[employee_id]
WHERE project_id IS NOT NULL
GROUP BY project_id 
