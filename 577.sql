SELECT name, bonus       
FROM Employee
LEFT JOIN Bonus on Employee.empId  = Bonus.empId
WHERE Bonus < 1000 or Bonus is NULL
