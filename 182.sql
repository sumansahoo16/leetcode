SELECT DISTINCT p.email 'Email'
FROM Person p
JOIN (
    SELECT email, COUNT(email) AS email_count
    FROM Person
    GROUP BY email
) c ON p.email = c.email
WHERE email_count  > 1 
