# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
Files added
  1.student.py
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
  2.member.py
    -class Member(Do a member role)
    -In a class Member, I have 7 methods:
      1. __init__ : To initialize the attributes of the class
      2. check_status : To check a status of a project.
      3. check_response : To check a response in member-request.csv.
      4. display_project : To display a project detail.
      5. display_choice : To display a choice for a member.
      6. display_input : To choose a project to update.
      7. update_information : To update a project information.
  3.admin.py
    - class Admin(Do a admin role)
    - In a class Admin, I have 4 methods:
      1. __init__ : To initialize the attributes of the class
      2. display_choice : To display a choice for a admin, to choose csv files to update information.
      3. display_input : To choose a column in csv file to update.
  4.lead.py
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
  5.faculty.py
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
  6.advisor.py
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

`There is a table of contents below for the project.`

| Role             | Action                                                                                                    | Relevant Class | Methods                                                                                                                                                                                                                                                                                   | Completion (%) |
|------------------|-----------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Admin            | Manage the database and update all tables                                                                 | Admin          | display_choice, display_input                                                                                                                                                                                                                                                             | 100            |
| Student          | Receive and respond to invitations, modify projects                                                       | Student        | find_project, check_pending_request, display_choice, create_project_and_become_lead, send_invitations                                                                                                                                                                                     | 100            |
| Lead Student     | Create project, find members, send invitations, add members, submit final project report                  | Lead           | find_project, check_member_name, check_status, check_response, display_project, display_choice, display_input, update_information, create_project, find_members, send_invitations, add_members_to_project, add_advisors_to_project, send_request_to_advisors, submit_final_project_report | 100            |
| Member Student   | See and modify project details                                                                            | Member         | check_status, check_response, display_project, display_choice, display_input, update_information                                                                                                                                                                                          | 100            |
| Normal Faculty   | See requests, send deny response, see all project details, evaluate projects                              | Faculty        | check_lead_id, check_lead_name,  display_choice,  see_requests, send_deny_response, check_pending_requests, project_details, evaluate_projects                                                                                                                                            | 100            |
| Advising Faculty | See requests, send accept or deny responses, see all project details, evaluate projects, approve projects | Advisor        | display_choice, see_requests, send_accept_response, send_deny_response, project_details, evaluate_projects, approve_projects                                                                                                                                                              | 100            |
