SELECT own.name as 'Employee'
FROM Employee own
JOIN Employee man on own.[managerId] = man.[id]
WHERE own.salary > man.salary
