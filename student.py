from database import Database
from database import Table


class Student:

    def __init__(self, database, _id):
        self.person_id = _id
        self.persons: Table = database.search('persons')
        self.project: Table = database.search('project')
        self.member_pending_request: Table = database.search('member-request')

    # Existing code...

    # Existing functions...

    def display_choice(self):
        while True:
            print("1. Invitational message") #See invitational message and acceept or deny
            print("2. Project's information")
            print("3. Update a project's information")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                pass


    def see_invitational_message(self):
        pending_invitations = self.member_pending_request.('member_id', self.person_id)
        for invitation in pending_invitations:
            lead_name = self.persons.find_by_id(invitation['lead_id'])['first'] + ' ' + \
                        self.persons.find_by_id(invitation['lead_id'])['last']
            print(f"You have received an invitation from {lead_name} for project {invitation['project_id']}")
            decision = input("Do you want to accept (A) or deny (D) the invitation? ").upper()
            if decision == 'A':
                self.accept_invitation(invitation['project_id'])
            elif decision == 'D':
                self.deny_invitation(invitation['project_id'])
            else:
                print("Invalid choice. Please enter 'A' to accept or 'D' to deny.")

    def accept_invitation(self, project_id):
        # Update MemberPendingRequest table
        self.member_pending_request.delete_by_columns({'member_id': self.person_id, 'project_id': project_id})

        # Update Project table (add member to the project)
        project = self.project.find_by_id(project_id)
        if project:
            if project['Member1'] == '':
                self.project.update(column='Member1', id=project_id, value=self.check_member_name())
            elif project['Member2'] == '':
                self.project.update(column='Member2', id=project_id, value=self.check_member_name())
            else:
                print("Project is already full. Cannot accept the invitation.")
                return
            print("Invitation accepted successfully.")
        else:
            print("Project not found.")

    def deny_invitation(self, project_id):
        # Update MemberPendingRequest table
        self.member_pending_request.delete_by_columns({'member_id': self.person_id, 'project_id': project_id})
        print("Invitation denied successfully.")

    def see_and_modify_project_details(self):

    # Existing code...

    def check_pending_requests(self):
        pending_requests = self.member_pending_request.find_by_column_value('member_id', self.person_id)
        if pending_requests:
            print("You have pending requests to join the following projects:")
            for request in pending_requests:
                project_title = self.project.find_by_id(request['project_id'])['Title']
                print(f"{project_title} (Project ID: {request['project_id']})")

            decision = input("Do you want to accept (A) or deny (D) these requests? ").upper()
            if decision == 'A':
                self.accept_pending_requests()
            elif decision == 'D':
                self.deny_pending_requests()
            else:
                print("Invalid choice. Please enter 'A' to accept or 'D' to deny.")

    def accept_pending_requests(self):
        pending_requests = self.member_pending_request.find_by_column_value('member_id', self.person_id)
        for request in pending_requests:
            self.accept_invitation(request['project_id'])

    def deny_pending_requests(self):
        pending_requests = self.member_pending_request.find_by_column_value('member_id', self.person_id)
        for request in pending_requests:
            self.deny_invitation(request['project_id'])

    def create_project_and_become_lead(self):
        # Existing code...

        # Deny all member requests first
        self.deny_pending_requests()

        # Create a project and become a lead
        new_project = self.create_project()
        self.become_lead(new_project['ID'])

    def send_requests_to_potential_members(self, project_id, potential_members):
        # Assume potential_members is a list of student IDs who can be invited
        for member_id in potential_members:
            request_data = {
                'project_id': project_id,
                'member_id': member_id,
                'status': 'pending'  # Request status
            }
            self.member_pending_request.insert(request_data)

    # Existing functions...
