from database import Table
from datetime import datetime


class Advisor:

    def __init__(self, database, person_id):
        self.person_id = person_id
        self.project: Table = database.search('project')
        self.advisor_request: Table = database.search('advisor-request')

    def display_choice(self):
        while True:
            print("1. Project details")
            print("2. See requests to be an advisor")
            print("3. Send an accept response")
            print("4. Send a deny response")
            print("5. Evaluate projects")
            print("6. Approve projects")
            print("7. Exit")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.project_details()
            elif choice == 2:
                self.see_requests()
            elif choice == 3:
                self.send_accept_response()
            elif choice == 4:
                self.send_deny_response()
            elif choice == 5:
                self.evaluate_projects()
            elif choice == 6:
                self.approve_projects()
            elif choice == 7:
                break
            else:
                print("Invalid choice. Try again.")
    def see_requests(self):
        pending_requests = self.advisor_request.filter(lambda x: x['Response'] == 'Pending' and x['to_be_advisor'] == self.person_id).table
        if pending_requests:
            print("Pending Requests:")
            for request in pending_requests:
                project_details = self.project.filter(lambda x: x['ID'] == request['ID']).table[0]
                print(f"Project ID: {project_details['ID']}, Title: {project_details['Title']}")
            print('')
        else:
            print("No pending requests.\n")

    def send_accept_response(self, project_id):
        self.advisor_request.update(column='Response', id=project_id, value='Accepted')
        self.advisor_request.update(column='Response_date', id=project_id, value=datetime.today().date())
        print(f"Accepted request for Project ID: {project_id}\n")

    def send_deny_response(self, project_id):
        self.advisor_request.update(column='Response', id=project_id, value='Denied')
        self.advisor_request.update(column='Response_date', id=project_id, value=datetime.today().date())
        print(f"Denied request for Project ID: {project_id}\n")

    def see_all_projects(self):
        print("All Projects:")
        for project in self.project.table:
            print(f"Project ID: {project['ID']}, Title: {project['Title']}, Status: {project['Status']}")
        print('')

    def evaluate_project(self, project_id):
        # Add your evaluation logic here
        print(f"Evaluating Project ID: {project_id}... (Placeholder for evaluation logic)\n")

    def approve_project(self, project_id):
        select_approve = input("Do you want to approve this project? (Y/N): ").upper()
        self.project.update(column='Status', id=project_id, value='Approved')
        print(f"Approved Project ID: {project_id}\n")

