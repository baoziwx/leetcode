/* Write your T-SQL query statement below */
select Person.FirstName, Person.LastName, Address.City, Address.State
from Person
left join Address on Person.PersonId = Address.PersonId
