# Write your MySQL query statement below
# delete p1 from person p1,person p2 
# where p1.email=p2.email and p1.id>p2.id;


DELETE p1 
FROM Person p1 
INNER JOIN Person p2 
WHERE p1.email = p2.email AND 
p1.id > p2.id;