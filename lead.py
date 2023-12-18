from database import Table
from datetime import datetime


class LeadStudent:

    def __init__(self, database, person_id):
        self.potential_members = None
        self.id_list = None
        self.person_id = person_id
        self.persons: Table = database.search('persons')
        self.project: Table = database.search('project')
        self.member_request: Table = database.search('member-request')
        self.advisor_request: Table = database.search('advisor-request')
        self.login: Table = database.search('login')

    def find_project(self):
        name = self.person_id
        for project in self.project.table:
            if name == project['Lead']:
                return project['ID']

    def check_member_name(self, id_):
        for person in self.persons.table:
            if id_ == person['ID']:
                return person['first'] + ' ' + person['last']

    def check_status(self):
        for project in self.project.table:
            if self.person_id in project.values():
                print(f'-{project["Title"]}: {project["Status"]}')

    def check_response(self):
        member_requests = []
        advisor_requests = []
        project_id = self.find_project()
        for request in self.member_request.table:
            if project_id == request['ID'] and request['Response'] == 'Accepted':
                member_requests.append(request)
        for request in self.advisor_request.table:
            if project_id == request['ID'] and request['Response'] == 'Accepted':
                advisor_requests.append(request)
        return member_requests, advisor_requests

    def display_project(self):
        self.id_list = []
        check_name = self.person_id
        for project in self.project.table:
            if check_name in project.values():
                self.id_list.append(project['ID'])
                print(f'Detail: {project}')

    def display_choice(self):
        while True:
            print("1. Project's status")
            print("2. Display a project's information")
            print("3. Update a project's information")
            print("4. All of your requests response")
            print("5. Create a project")
            print("6. Find members")
            print("7. Add members to project")
            print("8. ADD advisor to project")
            print("9. Send a request to students")
            print("10. Send a request to faculty")
            print("11. Submit final project report")
            print("12. Exit")
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
                check_name = self.person_id
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
                mem_response_list,advi_response_list = self.check_response()
                if mem_response_list == [] and advi_response_list == []:
                    print('You have no response')
                else:
                    for request in mem_response_list:
                        print('Your member request has response: ID.',request['ID'] + ' ' + request['Response'] + ' '
                              + request['Response_date'])
                    for request in advi_response_list:
                        print('Your advisor request has response: ID.',request['ID'] + ' ' + request['Response'] + ' '
                              + request['Response_date'])
                print('')
            elif choice == 5:
                print('-----Create a project-----')
                project = self.create_project()
                print('Your project: ID.', project['ID'] + ' ' + project['Title'] + ' ' + project['Status'])
                print('')
            elif choice == 6:
                print('-----Find your members-----')
                self.find_members()
                print('')
            elif choice == 7:
                self.add_members_to_project()
            elif choice == 8:
                self.add_advisor_to_project()
            elif choice == 9:
                print('-----Send a request to students-----')
                self.send_invitations()
                print('')
            elif choice == 10:
                print('-----Send a request to faculty-----')
                self.send_request_to_advisors()
                print('')
            elif choice == 11:
                print('-----Submit final project report-----')
                self.submit_final_project_report()
                print('')
            elif choice == 12:
                break

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
            'Lead': self.person_id,
            'Member1': '',
            'Member2': '',
            'Advisor': '',
            'Status': 'In Progress',
        }
        self.project.insert(project_details)
        return project_details

    def find_members(self):
        # Logic to find potential members, e.g., searching through a user table
        check_student = self.person_id
        for project in self.project.table:
            if check_student in project.values():
                print(f'ID:{project["ID"]}   {self.check_member_name(project["Member1"])}   '
                      f'{self.check_member_name(project["Member2"])}')

    def send_invitations(self):
        project_id = self.find_project()
        if self.project.filter(lambda x: x['ID'] == project_id).table[0]['Member1'] != '' \
                and self.project.filter(lambda x: x['ID'] == project_id).table[0]['Member2'] != '':
            print('Project is already full. Cannot send the invitation.')
            print('')
        while True:
            choice = input('Do you want to send a request to students (Y/N): ').upper()
            if choice == 'Y':
                for person in self.persons.table:
                    if person['type'] == 'student':
                        member_requests = {
                            'ID': project_id,
                            'to_be_member': person['ID'],
                            'Response': 'Pending',
                            'Response_date': datetime.today().date(),
                        }
                        self.member_request.insert(member_requests)
                print('----Your invitations have been sent----')
                print('')
                break
            elif choice == 'N':
                print('----Your invitations have not been sent----')
                print('')
                break
            else:
                print('Invalid choice. Please enter Y or N')
                print('--------------------------------')

    def add_members_to_project(self):
        requests = []
        project_id = self.find_project()
        for request in self.member_request.table:
            if project_id == request['ID'] and request['Response'] == 'Accepted':
                requests.append(request)
        if requests == []:
            print('***You have no response***')
            print('')
            return
        while True:
            n = 1
            for student in requests:
                print(f'{n}. ID: {student["ID"]} {self.check_member_name(student["to_be_member"])}')
                n += 1
            accept = input('Do you want to accept (A) or deny (D) these requests? ').upper()
            if requests == []:
                print('***You have no response***')
                print('')
                break
            print('(Or enter Q to quit)')
            print('---------------------')
            if accept == 'A':
                if requests == []:
                    print('***You have no response***')
                    print('')
                    break
                choice = input('Please select your choice: ')
                if 0 < int(choice) <= len(requests):
                    choice = int(choice)
                    if self.project.filter(lambda x: x['ID'] == project_id).table[0]['Member1'] == '':
                        self.project.update(column='Member1', id=project_id, value=requests[choice - 1]['to_be_member'])
                        print('Your member has been added in member1')
                        print('')
                        self.login.update(column='role', id=requests[choice - 1]['to_be_member'], value='member')
                        requests.pop(choice - 1)
                    elif self.project.filter(lambda x: x['ID'] == project_id).table[0]['Member2'] == '':
                        self.project.update(column='Member2', id=project_id, value=requests[choice - 1]['to_be_member'])
                        print('Your member has been added in member2')
                        print('')
                        requests.pop(choice - 1)
                    else:
                        print('Project is already full. Cannot accept the invitation.')
                elif choice == 'Q':
                    break
                else:
                    print('Please choose your member again')
            elif accept == 'D':
                if requests == []:
                    print('***You have no response***')
                    print('')
                    break
                choice = input('Please select your choice: ')
                if 0 < int(choice) <= len(requests):
                    choice = int(choice)
                    self.member_request.update(column='Response', id=requests[choice - 1]['ID'], value='Denied')
                    self.member_request.update(column='Response_date', id=requests[choice - 1]['ID'],
                                               value=datetime.today().date())
                    requests.pop(choice - 1)
                    print('Your member has been denied')
                break
            else:
                print('Invalid choice. Please enter A or D')
                print('--------------------------------')

    def add_advisor_to_project(self):
        requests = []
        project_id = self.find_project()
        for request in self.advisor_request.table:
            if project_id == request['ID'] and request['Response'] == 'Accepted':
                requests.append(request)
        if requests == []:
            print('***You have no response***')
            print('')
            return
        while True:
            n = 1
            for faculty in requests:
                print(f'{n}. ID: {faculty["ID"]} {self.check_member_name(faculty["to_be_member"])}')
                n += 1
            accept = input('Do you want to accept (A) or deny (D) these requests? ').upper()
            if requests == []:
                print('***You have no response***')
                print('')
                break
            print('(Or enter Q to quit)')
            if accept == 'A':
                choice = int(input('Please select your choice: '))
                if 0 < choice <= len(requests):
                    if self.project.filter(lambda x: x['ID'] == project_id).table[0]['Advisor'] == '':
                        self.project.update(column='Advisor', id=project_id, value=requests[choice - 1]['to_be_advisor'])
                        print('Your advisor has been added in a project')
                        requests.pop(choice - 1)
                    else:
                        print('Project is already full. Cannot accept the invitation.')
                elif choice == 'Q':
                    break
                else:
                    print('Please choose your advisor again')
            elif accept == 'D':
                choice = int(input('Please select your choice: '))
                if 0 < choice <= len(requests):
                    requests.pop(choice - 1)
                    print('Your advisor has been denied')
                break
            else:
                print('Invalid choice. Please enter A or D')
                print('--------------------------------')

    def send_request_to_advisors(self):
        project_id = self.find_project()
        if self.project.filter(lambda x: x['ID'] == project_id).table[0]['Advisor'] != '':
            print('This project already has an advisor. Cannot send the invitation.')
            print('')
        while True:
            choice = input('Do you want to send a request to faculty(Y/N): ').upper()
            if choice == 'Y':
                for person in self.persons.table:
                    if person['type'] == 'faculty':
                        faculty_requests = {
                            'ID': project_id,
                            'to_be_advisor': person['ID'],
                            'Response': 'Pending',
                            'Response_date': datetime.today().date(),
                        }
                        self.advisor_request.insert(faculty_requests)
                print('----Your invitations have been sent----')
                print('')
                break
            elif choice == 'N':
                print('----Your invitations have not been sent----')
                print('')
                break
            else:
                print('Invalid choice. Please enter Y or N')
                print('--------------------------------')

    def submit_final_project_report(self):
        while True:
            choice = input('Do you want to submit a final project report(Y/N): ').upper()
            if choice == 'Y':
                project_complete = []
                for project in self.project.table:
                    n = 1
                    if self.person_id in project['Lead']:
                        if project['Status'] == 'Completed':
                            print(f'{n} ID:{project["ID"]} {project["Title"]}')
                            n += 1
                            project_complete.append(project)
                if project_complete == []:
                    print('You have no project completed')
                    print('')
                    break
                while True:
                    choice = int(input('Please choose your project: '))
                    if 0 < choice <= len(project_complete):
                        self.project.update(column='Status', id=project_complete[choice - 1]['ID'], value='Submitted')
                        print('Your project has been submitted')
                        break
                    else:
                        print('Please choose your project again')
                        print('--------------------------------')
                break
            elif choice == 'N':
                print('----Your report has not been sent----')
                print('')
                break
            else:
                print('Invalid choice. Please enter Y or N')
                print('--------------------------------')


