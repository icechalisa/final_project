In database.py(contains the implementation of the Database and Table classes along with their methods.)
I have 2 classes: Database class, Table class

Database class
__init__ method: Initialize an empty list to store tables.
insert method: Add a table to the database.
search method: Searches for a table within the database based on its name.

Table class
__init__ method: Initialize a table with a name and initial data.
join method: Join two tables based on a common key.
filter method: Filter the table based on a given condition.
aggregate method: Apply an aggregation function to a specified key.
select method: Select specific attributes from the table.
insert method: Insert data into the table.
update method: Update a specific column in the table for a given ID.
__str__ method: Provide a string representation of the table.


In project_manage.py

data_file(f):  reads data from a CSV file (f) and transforms it into a list of dictionaries. 
initializing(): initializes the Database (database) by creating two tables (table and table2) 
using data from 'persons.csv' and 'login.csv'. It then inserts these tables into the database.

login(): prompts the user to enter a username and password. It then checks if the entered credentials match any user 
in the 'login.csv' file. If a match is found, it returns a list containing the user's ID and role. If no match is found, 
it returns None.

exit(f): writes the modified 'person' table from the database back to the CSV file specified by the parameter f. 
It retrieves the 'person' table from the database, iterates through each row, and writes the data to the CSV file.

