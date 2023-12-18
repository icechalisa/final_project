from database import Database
from database import Table
from datetime import datetime


class Student:

    def __init__(self, database, _id):
        self.person_id = _id
        self.persons: Table = database.search('persons')
        self.project: Table = database.search('project')
        self.member_request: Table = database.search('member-request')
        self.login: Table = database.search('login')

    def find_project(self):
        name = self.person_id
        for project in self.project.table:
            if name == project['Lead']:
                return project['ID']

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
            print("1. Invitational message")
            print("2. Create project")
            print("3. Exit")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.check_pending_requests()
            if choice == 2:
                return self.create_project_and_become_lead()
            elif choice == 3:
                break
            else:
                print('Invalid choice. Please enter 1-5')
                print('--------------------------------')

    def check_pending_requests(self):
        requests = []
        for request in self.member_request.table:
            if self.person_id == request['to_be_member'] and request['Response'] == 'Pending':
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
                    print(f'{n}. Project id:{student["ID"]} ,lead student:{self.check_lead_name(self.check_lead_id(student["ID"]))}')
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
                        for member in self.member_request.table:
                            if member['Response'] == 'Pending' and requests[choice - 1]['ID'] == member['ID']:
                                self.login.update(column='role', id=self.person_id, value='member')
                                self.member_request.update(column='Response', id=member['ID'], value='Accepted')
                                self.member_request.update(column='Response_date', id=member['ID'], value=datetime.today().date())
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
                        for member in self.member_request.table:
                            if member['Response'] == 'Pending' and requests[choice - 1]['ID'] == member['ID']:
                                self.member_request.update(column='Response', id=member['ID'], value='Denied')
                                self.member_request.update(column='Response_date', id=member['ID'], value=datetime.today().date())
                                requests.pop(choice - 1)
                                print('You have denied the requests')
                                break
                else:
                    print("Invalid choice. Please enter 'A' or 'D'")
                    print('---------------------------------')

    def create_project_and_become_lead(self):
        print(self.member_request.filter(lambda x: x['to_be_member'] == self.person_id).table)
        if self.member_request.filter(lambda x: x['to_be_member'] == self.person_id).table[0]['Response'] == 'Pending':
            print('You have to deny the request first')
            print('')
        elif self.member_request.filter(lambda x: x['to_be_member'] == self.person_id).table[0]['Response'] == 'Accepted':
            print('You have accepted the request, Cannot create a project')
            print('')
        elif self.member_request.filter(lambda x: x['to_be_member'] == self.person_id).table[0]['Response'] == 'Denied':
            print('----Create project----')
            project_details = {
                'ID': str(len(self.project.table) + 1),
                'Title': input('Please enter the title: '),
                'Lead': self.person_id,
                'Member1': '',
                'Member2': '',
                'Advisor': '',
                'Status': 'In Progress',
            }
            print('----Your project has been created----')
            self.project.insert(project_details)
            self.login.update(column='role', id=self.person_id, value='lead')
            return 'lead'

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


