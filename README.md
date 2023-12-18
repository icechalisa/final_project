# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv

## Files added

###### 1.student.py

    -class Student(Do a student role)
    -In a class Student, I have 13 methods:
      1. __init__ : To initialize the attributes of the class
      2. find_project : To find a project id.
      3. check_lead_id : To check a lead id.
      4. check_lead_name : To check a lead name.
      5. display_choice : To display a choice for a student.
      6. check_pending_request : To check a pending request which lead student sent.
      7. create_project_and_become_lead : To create a project and become a lead student.
      8. send_invitations : To send invitations to members.

###### 2.member.py

    -class Member(Do a member role)
    -In a class Member, I have 7 methods:
      1. __init__ : To initialize the attributes of the class
      2. check_status : To check a status of a project.
      3. check_response : To check a response in member-request.csv.
      4. display_project : To display a project detail.
      5. display_choice : To display a choice for a member.
      6. display_input : To choose a project to update.
      7. update_information : To update a project information.

###### 3.admin.py

    - class Admin(Do a admin role)
    - In a class Admin, I have 4 methods:
      1. __init__ : To initialize the attributes of the class
      2. display_choice : To display a choice for a admin, to choose csv files to update information.
      3. display_input : To choose a column in csv file to update.

######   4.lead.py

    - class Lead(Do a lead role)
    - In a class Lead, I have 16 methods:
      1. __init__ : To initialize the attributes of the class
      2. find_project : To find a project id which lead student in.
      3. check_member_name : To check a member name.
      4. check_status : To check a status of a project.
      5. check_response : To check a response in member-request.csv and advisor-request.csv.
      6. display_project : To display a project detail.
      7. display_choice : To display a choice for a lead student.
      8. display_input : To choose a project to update.
      9. update_information : To update a project information.
      10. create_project : To create a project.
      11. find_members : To find members to invite.
      12. send_invitations : To send invitations to student.
      13. add_members_to_project : To add members to project.
      14. add_advisors_to_project : To add advisors to project.
      15. send_request_to_advisors : To send request to advisors.
      16. submit_final_project_report : To submit final project report.

######   5.faculty.py

    - class Faculty(Do a faculty role)
    - In a class Faculty, I have 8 methods:
      1. check_lead_id : To check a lead id.
      2. check_lead_name : To check a lead name.
      3. display_choice : To display a choice for a faculty.
      4. see_requests : To see requests from lead students.
      5. send_deny_response : To send deny response to lead students.
      6. check_pending_request : To check a pending request which lead student sent.
      7. project_detail : To display a project detail.
      8. evaluate_projects : To evaluate projects.

######   6.advisor.py

    - class Advisor(Do a advisor role)
    - In a class Advisor, I have 7 methods:
      1. display_choice : To display a choice for a advisor.
      2. see_requests : To see requests from lead students.
      3. send_accept_response : To send accept response to lead students.
      4. send_deny_response : To send deny response to lead students.
      5. project_detail : To display a project detail.
      6. evaluate_projects : To evaluate projects.
      7. approve_projects : To approve projects.


To run and compile a project, you need to run project_manage.py
```commandline
python3 project_manage.py
```

### Table of each role's actions

`This table outlines the actions, relevant classes, and completion percentages for each role.`

| Role    | Action                                                        | Relevant Class | Methods                        | Completion (%) |
|---------|---------------------------------------------------------------|----------------|--------------------------------|----------------|
| Student | Initialize attributes of the class                            | Student        | __init__                       | 100            |
| Student | Find a project ID                                             | Student        | find_project                   | 100            |
| Student | Check a lead ID                                               | Student        | check_lead_id                  | 100            |
| Student | Check a lead name                                             | Student        | check_lead_name                | 100            |
| Student | Display a choice for a student                                | Student        | display_choice                 | 100            |
| Student | Check pending requests sent by the lead student               | Student        | check_pending_request          | 100            |
| Student | Create a project and become a lead student                    | Student        | create_project_and_become_lead | 100            |
| Student | Send invitations to members                                   | Student        | send_invitations               | 100            |
| Member  | Initialize attributes of the class                            | Member         | __init__                       | 100            |
| Member  | Check the status of a project                                 | Member         | check_status                   | 100            |
| Member  | Check a response in member-request.csv                        | Member         | check_response                 | 100            |
| Member  | Display project details                                       | Member         | display_project                | 100            |
| Member  | Display a choice for a member                                 | Member         | display_choice                 | 100            |
| Member  | Choose a project to update                                    | Member         | display_input                  | 100            |
| Member  | Update project information                                    | Member         | update_information             | 100            |
| Admin   | Initialize attributes of the class                            | Admin          | __init__                       | 100            |
| Admin   | Display a choice to choose CSV files to update information    | Admin          | display_choice                 | 100            |
| Admin   | Choose a column in a CSV file to update                       | Admin          | display_input                  | 100            |
| Lead    | Initialize attributes of the class                            | Lead           | __init__                       | 100            |
| Lead    | Find a project ID in which the lead student is involved       | Lead           | find_project                   | 100            |
| Lead    | Check a member name                                           | Lead           | check_member_name              | 100            |
| Lead    | Check the status of a project                                 | Lead           | check_status                   | 100            |
| Lead    | Check responses in member-request.csv and advisor-request.csv | Lead           | check_response                 | 100            |
| Lead    | Display project details                                       | Lead           | display_project                | 100            |
| Lead    | Display a choice for a lead student                           | Lead           | display_choice                 | 100            |
| Lead    | Choose a project to update                                    | Lead           | display_input                  | 100            |
| Lead    | Update project information                                    | Lead           | update_information             | 100            |
| Lead    | Create a project                                              | Lead           | create_project                 | 100            |
| Lead    | Find members to invite                                        | Lead           | find_members                   | 100            |
| Lead    | Send invitations to students                                  | Lead           | send_invitations               | 100            |
| Lead    | Add members to a project                                      | Lead           | add_members_to_project         | 100            |
| Lead    | Add advisors to a project                                     | Lead           | add_advisors_to_project        | 100            |
| Lead    | Send requests to advisors                                     | Lead           | send_request_to_advisors       | 100            |
| Lead    | Submit the final project report                               | Lead           | submit_final_project_report    | 100            |
| Faculty | Check a lead ID                                               | Faculty        | check_lead_id                  | 100            |
| Faculty | Check a lead name                                             | Faculty        | check_lead_name                | 100            |
| Faculty | Display a choice for a faculty                                | Faculty        | display_choice                 | 100            |
| Faculty | See requests from lead students                               | Faculty        | see_requests                   | 100            |
| Faculty | Send deny response to lead students                           | Faculty        | send_deny_response             | 100            |
| Faculty | Check pending requests sent by lead students                  | Faculty        | check_pending_request          | 100            |
| Faculty | Display project details                                       | Faculty        | project_detail                 | 100            |
| Faculty | Evaluate projects                                             | Faculty        | evaluate_projects              | 100            |
| Advisor | Display a choice for an advisor                               | Advisor        | display_choice                 | 100            |
| Advisor | See requests from lead students                               | Advisor        | see_requests                   | 100            |
| Advisor | Send accept response to lead students                         | Advisor        | send_accept_response           | 100            |
| Advisor | Send deny response to lead students                           | Advisor        | send_deny_response             | 100            |
| Advisor | Display project details                                       | Advisor        | project_detail                 | 100            |
| Advisor | Evaluate projects                                             | Advisor        | evaluate_projects              | 90             |
| Advisor | Approve projects                                              | Advisor        | approve_projects               | 100            |

### Class Database
(In database.py)

| Action                                  | Relevant Class | Methods   | Completion (%) |
|-----------------------------------------|----------------|-----------|----------------|
| Initialize Database                     | Database       | __init__  | 100            |
| Insert a Table into Database            | Database       | insert    | 100            |
| Search for a Table in Database          | Database       | search    | 100            |
| Create a Table with given parameters    | Table          | __init__  | 100            |
| Join two Tables based on a common key   | Table          | join      | 100            |
| Filter Table based on a given condition | Table          | filter    | 100            |
| Aggregate values in a Table             | Table          | aggregate | 100            |
| Select specific attributes from Table   | Table          | select    | 100            |
| Insert data into Table                  | Table          | insert    | 100            |
| Update values in Table                  | Table          | update    | 100            |
| Display Table as a String               | Table          | __str__   | 100            |


