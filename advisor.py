from database import Table
from datetime import datetime


class Advisor:

    def __init__(self, database, person_id):
        self.project_id = None
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
        pending_requests = self.advisor_request.filter(
            lambda x: x['Response'] == 'Pending' and x['to_be_advisor'] == self.person_id).table
        if pending_requests:
            print("Pending Requests:")
            for request in pending_requests:
                project_details = self.project.filter(lambda x: x['ID'] == request['ID']).table[0]
                print(f"Project ID: {project_details['ID']}, Title: {project_details['Title']}")
            print('')
        else:
            print("No pending requests.\n")

    def send_accept_response(self):
        self.advisor_request.update(column='Response', id=self.project_id, value='Accepted')
        self.advisor_request.update(column='Response_date', id=self.project_id, value=datetime.today().date())
        print(f"Accepted request for Project ID: {self.project_id}\n")

    def send_deny_response(self):
        self.advisor_request.update(column='Response', id=self.project_id, value='Denied')
        self.advisor_request.update(column='Response_date', id=self.project_id, value=datetime.today().date())
        print(f"Denied request for Project ID: {self.project_id}\n")

    def project_details(self):
        # Logic to see details of all projects
        projects = self.project.table
        if not projects:
            print("No projects available.")
        else:
            print("Project details:")
            for project in projects:
                print(
                    f"ID: {project['ID']}, Title: {project['Title']}, Lead: {project['Lead']}, "
                    f"Member1: {project['Member1']}, Member2: {project['Member2']}, Status: {project['Status']}")

    def evaluate_projects(self, project_id=None):
        project = self.project.filter(lambda x: x['ID'] == project_id).table[0]
        print(f"Project ID: {project['ID']}, Title: {project['Title']}, Lead: {project['Lead']}, "
              f"Member1: {project['Member1']}, Member2: {project['Member2']}, Status: {project['Status']}")
        print("1. Accept")
        print("2. Reject")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            self.project.update(column='Status', id=project_id, value='Accepted')
            print(f"Accepted Project ID: {project_id}\n")
        elif choice == 2:
            self.project.update(column='Status', id=project_id, value='Rejected')
            print(f"Rejected Project ID: {project_id}\n")
        else:
            print("Invalid choice. Try again.")

    def approve_projects(self):
        for project in self.project.table:
            if project['ID'] == self.project_id and project['Status'] == 'Completed':
                project['Status'] = 'Approved'
                print(f"Approved Project ID: {self.project_id}\n")
                break
