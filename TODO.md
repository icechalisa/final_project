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

Student Role (student.py)
Methods:
__init__: Initialize the attributes of the class.
find_project: Find a project ID.
check_lead_id: Check a lead ID.
check_lead_name: Check a lead name.
display_choice: Display a choice for a student.
check_pending_request: Check pending requests sent by the lead student.
create_project_and_become_lead: Create a project and become a lead student.
send_invitations: Send invitations to members.

Member Role (member.py)
Methods:
__init__: Initialize the attributes of the class.
check_status: Check the status of a project.
check_response: Check responses in member-request.csv.
display_project: Display project details.
display_choice: Display a choice for a member.
display_input: Choose a project to update.
update_information: Update project information.

Admin Role (admin.py)
Methods:
__init__: Initialize the attributes of the class.
display_choice: Display a choice for an admin to choose CSV files to update information.
display_input: Choose a column in a CSV file to update.

Lead Role (lead.py)
Methods:
__init__: Initialize the attributes of the class.
find_project: Find a project ID in which the lead student is involved.
check_member_name: Check a member name.
check_status: Check the status of a project.
check_response: Check responses in member-request.csv and advisor-request.csv.
display_project: Display project details.
display_choice: Display a choice for a lead student.
display_input: Choose a project to update.
update_information: Update project information.
create_project: Create a project.
find_members: Find members to invite.
send_invitations: Send invitations to students.
add_members_to_project: Add members to a project.
add_advisors_to_project: Add advisors to a project.
send_request_to_advisors: Send requests to advisors.
submit_final_project_report: Submit the final project report.

Faculty Role (faculty.py)
Methods:
check_lead_id: Check a lead ID.
check_lead_name: Check a lead name.
display_choice: Display a choice for a faculty.
see_requests: See requests from lead students.
send_deny_response: Send deny responses to lead students.
check_pending_request: Check pending requests sent by the lead student.
project_detail: Display project details.
evaluate_projects: Evaluate projects.
Advisor Role (advisor.py)
Methods:
display_choice: Display a choice for an advisor.
see_requests: See requests from lead students.
send_accept_response: Send accept responses to lead students.
send_deny_response: Send deny responses to lead students.
project_detail: Display project details.
evaluate_projects: Evaluate projects.
approve_projects: Approve projects.


In project_manage.py

data_file(f):  reads data from a CSV file (f) and transforms it into a list of dictionaries. 
initializing(): initializes the Database (database) by creating two tables (table and table2) 
using data from 'persons.csv' and 'login.csv'. It then inserts these tables into the database.

login(): prompts the user to enter a username and password. It then checks if the entered credentials match any user 
in the 'login.csv' file. If a match is found, it returns a list containing the user's ID and role. If no match is found, 
it returns None.

exit(f): writes the modified 'person' table from the database back to the CSV file specified by the parameter f. 
It retrieves the 'person' table from the database, iterates through each row, and writes the data to the CSV file.

