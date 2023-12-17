from database import Table

class LeadStudent:

    def __init__(self, database):
        self.id_list = None
        self.person_id = None
        self.persons: Table = database.search('persons')
        self.project: Table = database.search('project')
        self.member_request: Table = database.search('member-request')
        self.advisor_request: Table = database.search('advisor-request')

    def check_member_name(self):
        for person in self.persons.table:
            if self.person_id == person['ID']:
                return person['first'] + ' ' + person['last']

    def check_status(self):
        check_name = self.check_member_name()
        for project in self.project.table:
            if check_name in project.values():
                print(f'-{project["Title"]}: {project["Status"]}')

    def check_response(self):
        requests = []
        for request in self.member_request.table:
            if self.check_member_name() == request['to_be_member']:
                requests.append(request)
        return requests

    def display_project(self):
        self.id_list = []
        check_name = self.check_member_name()
        for project in self.project.table:
            if check_name in project.values():
                self.id_list.append(project['ID'])
                print(f'Detail: {project}')

    def display_choice(self):
        while True:
            print("1. Project's status")
            print("2. Display a project's information")
            print("3. Update a project's information")
            print("4. All requests")
            print("5. Create a project")
            print("6. Find members")
            print("7. Add members to project")
            print("8. Send a request to students")
            print("9. Send a request to faculty")
            print("10. Submit final project report")
            print("11. Exit")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                print('-----Project status-----')
                self.check_status()
                print('')
            elif choice == 2:
                print('-----Project information-----')
                self.display_project()
                print('')
            elif choice == 3:
                print('-----Update project information-----')
                self.id_list = []
                check_name = self.check_member_name()
                self.my_project = []
                n = 1
                for project in self.project.table:
                    if check_name in project.values():
                        self.id_list.append(project['ID'])
                        print(f'{n}. Detail: {project}')
                        self.my_project.append(project)
                        n += 1

                self.display_input('project', self.project, self.my_project)
                self.update_information()
                print('')
            elif choice == 4:
                print('-----All requests-----')
                for request in self.check_response():
                    print('Your request: ', request['ID'] + ' ' + request['Response'] + ' ' + request['Response_date'])
                print('')
            elif choice == 5:
                print('-----Create a project-----')
                self.create_project(self.project.table)
                print('')
            elif choice == 6:
                print('-----Find members-----')
                print('Students who can be a member: ')
                self.find_members()
                print('')

    def display_input(self, file, table, my_project):
        while True:
            selected_project = int(input('Please choose your project: '))
            if 0 < selected_project <= len(my_project):
                self.id = my_project[selected_project - 1]['ID']
                while True:
                    self.column = input("Please enter the column name: ")
                    if self.column in table.table[0].keys():
                        break
                    else:
                        print("Column is not exist")
                while True:
                    self.value = input("Please enter the new value: ")
                    if self.value != '':
                        break
                    else:
                        print("Value is not exist")
                break
            else:
                print('Please choose your project again')
                print('--------------------------------')

    def update_information(self):
        print('New information', self.project.table)
        if self.column in self.project.table[0].keys():
            self.project.update(
                column=self.column,
                id=self.id,
                value=self.value
            )
            print(self.project.table)
            return True
        else:
            print("Column is not exist")
            return False
    def create_project(self):
        project_details = {
            'ID': str(len(self.project.table) + 1),
            'Title': input('Please enter the title: '),
            'Lead': input('Please enter your name: '),
            'Member1': input('Please enter the first member: '),
            'Member2': input('Please enter the second member: '),
            'Advisor': input('Please enter the advisor: '),
            'Status': input('Please enter the status: ')
        }
        self.project.insert(project_details)
        return self.project

    def find_members(self):
        # Logic to find potential members, e.g., searching through a user table
        check_student = self.check_member_name()
        for project in self.project.table:
            if check_student in project.values():
                print(project['ID'] + ' ' + project['Member1'] + ' ' + project['Member2'])

    def send_invitations(self, project_id, potential_members):
        # Assume potential_members is a list of member IDs
        for member_id in potential_members:
            invitation_data = {
                'project_id': project_id,
                'member_id': member_id,
                'status': 'pending'  # Invitation status
            }
            self.member_request.insert(invitation_data)

    def add_members_to_project(self, project_id, member_ids):
        # Assume member_ids is a list of member IDs to be added to the project
        # Add members to the project, update the project table, etc.
        # ...


    def see_and_modify_project_details(self, project_id):
        # Retrieve and display project details
        project_details = self.project.find_by_id(project_id)
        print("Current Project Details:", project_details)

        # Logic to modify project details
        # ...

    def send_request_to_advisors(self, project_id, advisor_ids):
        # Assume advisor_ids is a list of advisor IDs to whom requests are sent
        for advisor_id in advisor_ids:
            request_data = {
                'project_id': project_id,
                'advisor_id': advisor_id,
                'status': 'pending'  # Request status
            }
            self.advisor_request.insert(request_data)

    def submit_final_project_report(self, project_id, report_data):
        # Assume report_data is a dictionary containing the final project report
        # Update the project table with the final report
        self.project.update(column='report', id=project_id, value=report_data)
        print("Final project report submitted successfully.")
