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
    - 
  5.faculty.py
    - class Faculty(Do a faculty role)
  6.advisor.py
    - class Advisor(Do a advisor role)

To run and compile a project, you need to run project_manage.py

There is a table 
| Role               | Action                              | Methods                                              | Classes                              | Completion (%) |
|--------------------|-------------------------------------|------------------------------------------------------|--------------------------------------|----------------|
| Admin              | Manage Database                     | - `display_choice`                                    | - `Admin`                         |100%            |
| Student            | Respond to Lead Invitation          | - `respond_to_invitation`                           | - `LeadStudent`                      | 90%            |
|                    | View and Modify Project Details      | - `view_project_details`                            | - `LeadStudent`                      | 100%           |
| Lead Student       | Create Project                       | - `create_project`                                  | - `LeadStudent`                      | 90%            |
|                    | Find Members                         | - `find_members`                                   | - `LeadStudent`                      | 100%           |
|                    | Send Invitations to Members          | - `send_invitations`                               | - `LeadStudent`                      | 80%            |
|                    | Add Members to Project               | - `add_members_to_project`                         | - `LeadStudent`                      | 70%            |
|                    | Send Requests to Advisors            | - `send_request_to_advisors`                      | - `LeadStudent`                      | 60%            |
|                    | Submit Final Project Report          | - `submit_final_project_report`                    | - `LeadStudent`                      | 100%           |
| Member Student     | View and Modify Project Details      | - `view_project_details`                            | - `LeadStudent`                      | 100%           |
| Normal Faculty     | Respond to Advisor Request           | - `respond_to_advisor_request`                     | - `NormalFaculty`                    | 90%            |
|                    | View Project Details                 | - `view_all_projects`                              | - `NormalFaculty`                    | 100%           |
|                    | Evaluate Projects                    | - (Explanation in proposal)                         | - `NormalFaculty`                    | (To be proposed) |
| Advising Faculty   | Respond to Advisor Request           | - `respond_to_advisor_request`                     | - `AdvisingFaculty`                  | 90%            |
|                    | View Project Details                 | - `view_all_projects`                              | - `AdvisingFaculty`                  | 100%           |
|                    | Evaluate Projects                    | - (Explanation in proposal)                         | - `AdvisingFaculty`                  | (To be proposed) |
|                    | Approve Project                      | - `approve_project`                                | - `AdvisingFaculty`                  | 70%            |
