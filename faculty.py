from database import Table
from datetime import datetime


class Faculty:

    def __init__(self, database, person_id):
        self.login = None
        self.persons = None
        self.person_id = person_id
        self.project: Table = database.search('project')
        self.advisor_request: Table = database.search('advisor-request')
        
    def check_lead_id(self, id_):
        for lead_id in self.project.table:
            if id_ == lead_id['ID']:
                return lead_id['Lead']

    def check_lead_name(self, id_):
        for person in self.persons.table:
            if id_ == person['ID']:
                return person['first'] + ' ' + person['last']

    def display_choice(self):
        while True:
            print("1. Project details")
            print("2. See requests to be an advisor")
            print("3. Send a deny response")
            print("4. Evaluate projects")
            print("5. Exit")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.project_details()
            elif choice == 2:
                self.check_pending_requests()
            elif choice == 3:
                self.send_deny_response()
            elif choice == 4:
                self.evaluate_projects()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Try again.")

    def see_requests(self):
        requests = self.advisor_request.filter(lambda x: x['to_be_advisor'] == self.person_id)
        if not requests:
            print("No requests to be an advisor.")
        else:
            print("Requests to be an advisor:")
            for request in requests:
                print(f"Project ID: {request['ID']}, Student ID: {request['to_be_advisor']}")

    def send_deny_response(self):
        requests = self.advisor_request.filter(
            lambda x: x['to_be_advisor'] == self.person_id and x['Response'] == 'Pending')
        if not requests:
            print("You don't have any pending requests.")
        else:
            print("----Pending requests----")
            for request in requests:
                print(f"Project ID: {request['ID']}, Student ID: {request['to_be_advisor']}")
            while True:
                project_id = input("Enter the Project ID to deny the request (or 'Q' to quit): ")
                if project_id.upper() == 'Q':
                    break
                else:
                    request = self.advisor_request.filter(
                        lambda x: x['ID'] == project_id and x['Response'] == 'Pending')
                    if request:
                        request = request[0]
                        request['Response'] = 'Denied'
                        request['Response_date'] = datetime.today().date()
                        print("Request denied.")
                        break
                    else:
                        print("Invalid Project ID. Try again.")

    def check_pending_requests(self):
        requests = []
        for request in self.advisor_request.table:
            if request['Response'] == 'Pending':
                requests.append(request)
        if requests == []:
            print("***You have no pending requests***")
            print('')
            return
        else:
            print('-----Pending requests-----')
            while True:
                n = 1
                for student in requests:
                    print(f'{n}. Project id:{student["ID"]} ,'
                          f'lead student:{self.check_lead_name(self.check_lead_id(student["ID"]))}')
                    n += 1
                decision = input("Do you want to accept (A) or deny (D) these requests? ").upper()
                print('(Or enter Q to quit)')
                if decision == 'A':
                    if requests == []:
                        print("***You have no pending requests***")
                        print('')
                        return
                    choice = (input('Please select your choice: '))
                    if 0 < int(choice) <= len(requests):
                        choice = int(choice)
                        for advisor in self.advisor_request.table:
                            if advisor['Response'] == 'Pending' and requests[choice - 1]['ID'] == advisor['ID']:
                                self.login.update(column='role', id=self.person_id, value='member')
                                self.advisor_request.update(column='Response', id=advisor['ID'], value='Accepted')
                                self.advisor_request.update(column='Response_date', id=advisor['ID'], value=datetime.today().date())
                                requests.pop(choice - 1)
                                print('You have accepted the requests')
                                break
                    elif decision == 'Q':
                        break
                    else:
                        print("Please select your choice again")
                        print('---------------------------------')
                elif decision == 'D':
                    if requests == []:
                        print("***You have no pending requests***")
                        print('')
                        return
                    choice = input('Please select your choice: ')
                    if 0 < int(choice) <= len(requests):
                        choice = int(choice)
                        for advisor in self.advisor_request.table:
                            if advisor['Response'] == 'Pending' and requests[choice - 1]['ID'] == advisor['ID']:
                                self.advisor_request.update(column='Response', id=advisor['ID'], value='Denied')
                                self.advisor_request.update(column='Response_date', id=advisor['ID'], value=datetime.today().date())
                                requests.pop(choice - 1)
                                print('You have denied the requests')
                                break
                else:
                    print("Invalid choice. Please enter 'A' or 'D'")
                    print('---------------------------------')

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

    def evaluate_projects(self):
        projects = self.project.table
        if not projects:
            print("No projects available for evaluation.")
        else:
            print("Evaluate projects:")
            for project in projects:
                print(
                    f"ID: {project['ID']}, Title: {project['Title']}, Lead: {project['Lead']}, Status: {project['Status']}")
                evaluation = input("Enter your evaluation for the project (or 'Q' to quit): ")
                if evaluation.upper() == 'Q':
                    break
                else:
                    print("Evaluation submitted.")

