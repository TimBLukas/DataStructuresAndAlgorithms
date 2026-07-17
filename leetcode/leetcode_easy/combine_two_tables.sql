# Leetcode 175: Combine two tables

# Write a solution to report the first name, last name, city, and state of each person in the Person table.
# If the address of a personId is not present in the Address table, report null instead.
# Return the result table in any order.


SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT OUTER JOIN Address ON Person.personId = Address.personId;